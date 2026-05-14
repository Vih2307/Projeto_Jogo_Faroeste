import os
import random
import time
from entidades.entidade import Entidade
from entidades.inimigo import Inimigo, Inimigos
from entidades.jogador import Jogador
from classes_jogador.classe import CLASSES_FAROESTE
from vocacoes.vocacao import VOCACOES_FAROESTE
from sistema_dados.dados import SistemaDados
from combate.combate import Combate
from eventos.eventro_trem import evento_assalto_trem
from eventos.evento_bau import evento_bau
import ui
import threading


def criar_personagem():
    ui.tela_titulo()
    
    ui.imprimir_lento("O sol do meio-dia castiga a terra rachada...", cor="yellow")
    ui.imprimir_lento("O vento quente traz o cheiro de pólvora e uísque barato.", cor="yellow")
    ui.imprimir_lento("Engraxe suas botas. Sua história começa agora!\n", cor="bold yellow")
    time.sleep(1)

    nome = ui.receber_input("Me diga seu nome Cowboy!\nNome: ").title()

    ui.console.print(f"\n[bold green]Escolha sua CLASSE {nome}:[/bold green]")
    classes = list(CLASSES_FAROESTE.keys())

    opcoes_classes = {}
    for i, c in enumerate(classes):
        ui.console.print(f"[bold cyan]{c}[/bold cyan]: Poder: {CLASSES_FAROESTE[c]['poder']} | Defesa: {CLASSES_FAROESTE[c]['defesa']} | Vida: {CLASSES_FAROESTE[c]['vida']} | Munição: {CLASSES_FAROESTE[c]['muniçao']}")
        opcoes_classes[c] = str(i + 1)

    escolha_classe_str = ui.receber_escolha("\nEscolha sua classe clicando abaixo:", opcoes_classes)
    try:
        escolha_classe = int(escolha_classe_str) - 1
    except:
        escolha_classe = 0
        
    if escolha_classe < 0 or escolha_classe >= len(classes): escolha_classe = 0
    classe_nome = classes[escolha_classe]
    classe_stats = CLASSES_FAROESTE[classe_nome]

    ui.console.print("\n[bold green]Agora escolha sua VOCAÇÃO:[/bold green]")
    vocacoes = list(VOCACOES_FAROESTE.keys())

    opcoes_vocacoes = {}
    for i, v in enumerate(vocacoes):
        ui.console.print(f"[bold cyan]{v}[/bold cyan]: Poder: {VOCACOES_FAROESTE[v]['poder']} | Defesa: {VOCACOES_FAROESTE[v]['defesa']} | Vida: {VOCACOES_FAROESTE[v]['vida']} | Munição: {VOCACOES_FAROESTE[v]['muniçao']} | Item: {VOCACOES_FAROESTE[v]['item']}")
        opcoes_vocacoes[v] = str(i + 1)

    escolha_vocacao_str = ui.receber_escolha("\nEscolha sua vocação clicando abaixo:", opcoes_vocacoes)
    try:
        escolha_vocacao = int(escolha_vocacao_str) - 1
    except:
        escolha_vocacao = 0
        
    if escolha_vocacao < 0 or escolha_vocacao >= len(vocacoes): escolha_vocacao = 0
    vocacao_nome = vocacoes[escolha_vocacao]
    vocacao_stats = VOCACOES_FAROESTE[vocacao_nome]

    # Atributos Iniciais
    poder = classe_stats["poder"] + vocacao_stats["poder"]
    defesa = classe_stats["defesa"] + vocacao_stats["defesa"]
    vida_max = classe_stats["vida"] + vocacao_stats["vida"]
    municao = classe_stats["muniçao"] + vocacao_stats["muniçao"]
    esquiva = 10  # Base de esquiva

    inventario = {"Bandagem": 3, "Uísque": 1, "Dinamite": 1}
    if "item" in vocacao_stats:
        inventario[vocacao_stats["item"]] = 1

    jogador = Jogador(
        nome=nome,
        poder=poder,
        defesa=defesa,
        vida_maxima=vida_max,
        vida_atual=vida_max,
        esquiva=esquiva,
        muniçao=municao,
        nivel=1,
        exp=0,
        raca=classe_nome,
        vocacao=vocacao_nome,
        inventario=inventario
    )

    return jogador


def escolher_inimigo_por_nivel(nivel_jogador):
    dificuldades_permitidas = ["Facil"]

    if nivel_jogador >= 3:
        dificuldades_permitidas.append("Médio")

    if nivel_jogador >= 5:
        if "Facil" in dificuldades_permitidas:
            dificuldades_permitidas.remove("Facil")
        dificuldades_permitidas.append("Difícil")

    inimigos_possiveis = [nome for nome, stats in Inimigos.items(
    ) if stats["dificuldade"] in dificuldades_permitidas]

    return random.choice(inimigos_possiveis)


def menu_principal(jogador):
    dados = SistemaDados()

    while True:
        ui.limpar_tela()
        ui.mostrar_cabecalho(jogador)
        ui.console.print("\n[bold]O que você vai fazer, parceiro?[/bold]", justify="center")
        
        opcoes_menu = {
            "🏇 Viajar": "1",
            "🌍 Explorar": "2",
            "🎒 Conferir Sela": "3",
            "🚪 Sair": "4"
        }
        escolha = ui.receber_escolha("", opcoes_menu)

        if escolha == "1":
            # Escolher inimigo aleatório
            nome_inimigo = escolher_inimigo_por_nivel(jogador.nivel)
            stats = Inimigos[nome_inimigo]
            dados_inimigo = Inimigos[nome_inimigo]
            inimigo = Inimigo(
                nome=nome_inimigo,
                poder=stats["poder"],
                defesa=stats["defesa"],
                vida_maxima=stats["vida"],
                vida_atual=stats["vida"],
                esquiva=stats["esquiva"],
                exp_recompensa=stats["exp_recompensa"],
                dificuldade=stats["dificuldade"],
                historia=dados_inimigo.get("historia", ""),
                falas=dados_inimigo.get("falas", {})
            )

            combate = Combate(jogador, inimigo)
            vivo = combate.iniciar_combate()

            if not vivo:
                ui.console.print("\n[bold red]FIM DE JOGO![/bold red]")
                break
            
            ui.esperar_enter()

        elif escolha == "2":
            ui.limpar_tela()
            ui.mostrar_cabecalho(jogador)
            rolagem = dados.rolar_d20()
            ui.mensagem_evento("Explorando...", f"Você rolou o dado e tirou: [bold yellow]{rolagem}[/bold yellow]", "cyan")
            time.sleep(1)

            if rolagem >= 18:
                img_path = r"C:\Users\vinic\.gemini\antigravity\brain\e6a79699-bf18-4c87-982a-2d49a9e99e21\ladrao_bandoleiro_1778028056322.png" # Proxy pra trem
                ui.mostrar_imagem(img_path)
                if not evento_assalto_trem(jogador, dados):
                    break

            elif rolagem >= 12:
                img_path = r"C:\Users\vinic\.gemini\antigravity\brain\e6a79699-bf18-4c87-982a-2d49a9e99e21\sela_faroeste_1778026536324.png" # Proxy pra bau
                ui.mostrar_imagem(img_path)
                if not evento_bau(jogador, dados):
                    break

            elif rolagem >= 5:
                ui.mensagem_evento("Pousada Simples", "Você encontrou uma cidade pacífica e descansou um pouco. Curou 10 de HP.", "green")
                jogador.curar(10)
                time.sleep(2)

            else:
                ui.console.print("[bold red]Você foi emboscado enquanto explorava![/bold red]")
                time.sleep(1)
                nome_inimigo = escolher_inimigo_por_nivel(jogador.nivel)
                stats = Inimigos[nome_inimigo]
                inimigo = Inimigo(nome_inimigo, stats["poder"], stats["defesa"], stats["vida"],
                                  stats["vida"], stats["esquiva"], stats["exp_recompensa"], stats["dificuldade"], stats.get("historia", ""), stats.get("falas", {}))
                combate = Combate(jogador, inimigo)
                if not combate.iniciar_combate():
                    break
            
            ui.esperar_enter()

        elif escolha == "3":
            ui.mostrar_inventario(jogador)
            ui.esperar_enter()

        elif escolha == "4":
            ui.console.print("[bold cyan]Até a próxima, parceiro! O deserto não perdoa...[/bold cyan]")
            break
        else:
            ui.console.print("[red]Opção inválida![/red]")
            time.sleep(1)


def iniciar_jogo():
    player = criar_personagem()
    menu_principal(player)
    ui.gui.root.quit()

if __name__ == "__main__":
    t = threading.Thread(target=iniciar_jogo, daemon=True)
    t.start()
    ui.gui.start()
