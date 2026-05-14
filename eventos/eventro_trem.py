import random
import time

from combate.combate import Combate
from entidades.inimigo import Inimigo, Inimigos
import ui


def evento_assalto_trem(jogador, dados):
    ui.limpar_tela()
    ui.mensagem_evento("🚂 ASSALTO AO TREM 🚂", "Ao longe, você vê a fumaça escura de uma locomotiva cortando o deserto.", "red")
    time.sleep(1)
    ui.console.print("\n[italic yellow]O trem passa carregado de suprimentos, munição e talvez algo mais valioso...[/italic yellow]")
    time.sleep(1)
    ui.console.print("\n[bold]Uma oportunidade dessas não aparece duas vezes.[/bold]")

    escolha_inicial = ui.receber_input("\nDeseja tentar assaltar o trem? (s/n): ").strip().lower()

    if escolha_inicial != "s":
        ui.console.print("[gray]Você decide não arriscar. O trem desaparece no horizonte...[/gray]")
        ui.esperar_enter()
        return True

    opcoes = {
        "Subir sorrateiramente pelos fundos": "1",
        "Pular para um vagão em movimento": "2",
        "Sacar a arma e ataque frontal": "3"
    }
    escolha = ui.receber_escolha("\nComo você quer agir?", opcoes)

    bonus = 0
    tipo_abordagem = ""

    if escolha == "1":
        tipo_abordagem = "furtiva"
        bonus = 2
        ui.console.print("\n[italic]Você cavalga por trás da locomotiva, tentando subir sem ser notado...[/italic]")
    elif escolha == "2":
        tipo_abordagem = "ousada"
        bonus = 0
        ui.console.print("\n[italic]Você acelera o cavalo e tenta saltar direto para um dos vagões...[/italic]")
    elif escolha == "3":
        tipo_abordagem = "frontal"
        bonus = -2
        ui.console.print("\n[italic]Você parte pra cima sem medo, arma em punho e sangue nos olhos![/italic]")
    else:
        ui.console.print("[red]Você hesitou demais. O trem passou e a chance foi perdida.[/red]")
        ui.esperar_enter()
        return True

    ui.console.print("\nVocê tenta entrar no trem...")
    ui.esperar_enter()
    rolagem_entrada = dados.rolar_d20() + bonus
    ui.console.print(f"Rolagem de entrada: [bold cyan]{rolagem_entrada}[/bold cyan] (com modificador {bonus})")

    if rolagem_entrada < 10:
        ui.console.print("\n[bold red]Você falhou na aproximação![/bold red]")
        if tipo_abordagem == "furtiva":
            ui.console.print("Um dos guardas percebeu sua movimentação e você precisou recuar.")
        elif tipo_abordagem == "ousada":
            ui.console.print("Você errou o salto e caiu na areia com violência.")
            jogador.receber_dano(8)
        else:
            ui.console.print("Os guardas reagiram rápido e abriram fogo contra você.")
            jogador.receber_dano(12)
        ui.esperar_enter()
        return True

    ui.console.print("\n[bold green]Você conseguiu entrar no trem![/bold green]")

    ui.console.print("\nAgora você precisa lidar com a segurança do vagão...")
    ui.esperar_enter()
    rolagem_confronto = dados.rolar_d20() + bonus
    ui.console.print(f"Rolagem de confronto: [bold cyan]{rolagem_confronto}[/bold cyan] (com modificador {bonus})")

    if rolagem_confronto < 8:
        ui.console.print("\n[bold red]Você foi surpreendido pelos guardas do trem![/bold red]")
        ui.console.print("Um homem armado surge entre os caixotes e bloqueia seu caminho.")

        nome_guarda = "Guarda do Trem"
        stats = Inimigos[nome_guarda]

        inimigo = Inimigo(
            nome_guarda,
            stats["poder"],
            stats["defesa"],
            stats["vida"],
            stats["vida"],
            stats["esquiva"],
            stats["exp_recompensa"],
            stats["dificuldade"],
            stats.get("historia", ""),
            stats.get("falas", {})
        )

        ui.esperar_enter()
        combate = Combate(jogador, inimigo)
        if not combate.iniciar_combate():
            return False

        ui.limpar_tela()
        ui.console.print("\n[bold green]Depois do confronto, você revira o vagão às pressas.[/bold green]")
        ui.console.print("Você encontrou algumas provisões antes de saltar do trem.")
        jogador.muniçao += 10
        jogador.inventario["Bandagem"] = jogador.inventario.get("Bandagem", 0) + 1
        ui.console.print("[yellow]+10 munições[/yellow]")
        ui.console.print("[yellow]+1 Bandagem[/yellow]")
        ui.esperar_enter()
        return True

    elif rolagem_confronto < 15:
        ui.console.print("\n[bold green]Você neutralizou os obstáculos e saqueou parte da carga.[/bold green]")

        recompensa = random.randint(1, 3)

        if recompensa == 1:
            ui.console.print("Você encontrou um caixote de munição.")
            jogador.muniçao += 20
            ui.console.print("[yellow]+20 munições[/yellow]")

        elif recompensa == 2:
            ui.console.print("Você encontrou suprimentos médicos escondidos no vagão.")
            jogador.inventario["Bandagem"] = jogador.inventario.get("Bandagem", 0) + 2
            ui.console.print("[yellow]+2 Bandagens[/yellow]")

        else:
            ui.console.print("Você encontrou documentos valiosos e os vendeu depois.")
            jogador.ganhar_exp(100)
            ui.console.print("[yellow]+100 EXP[/yellow]")

        ui.esperar_enter()
        return True

    else:
        ui.console.print("\n[bold magenta]Você executou um assalto quase perfeito![/bold magenta]")
        ui.console.print("Depois de dominar o vagão principal, você encontra uma carga valiosa.")

        recompensa_grande = random.randint(1, 3)

        jogador.ganhar_exp(150)

        if recompensa_grande == 1:
            jogador.muniçao += 35
            jogador.inventario["Bandagem"] = jogador.inventario.get("Bandagem", 0) + 2
            ui.console.print("[yellow]+35 munições[/yellow]")
            ui.console.print("[yellow]+2 Bandagens[/yellow]")

        elif recompensa_grande == 2:
            jogador.muniçao += 25
            jogador.inventario["Bandagem"] = jogador.inventario.get("Bandagem", 0) + 3
            jogador.curar(15)
            ui.console.print("[yellow]+25 munições[/yellow]")
            ui.console.print("[yellow]+3 Bandagens[/yellow]")

        else:
            jogador.muniçao += 40
            ui.console.print("[yellow]+40 munições[/yellow]")
            ui.console.print("Você encontrou uma carga rara e saiu do trem com fama ainda maior.")
            jogador.ganhar_exp(50)

        ui.console.print("\n[italic gray]Antes que reforços apareçam, você salta do trem e desaparece no deserto.[/italic gray]")
        ui.esperar_enter()
        return True
