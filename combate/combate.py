import random
from sistema_dados.dados import SistemaDados
import ui
import time


class Combate:
    def __init__(self, jogador, inimigo):

        self.jogador = jogador
        self.inimigo = inimigo
        self.dados = SistemaDados()

    def mostrar_fala_inimigo(self, situacao):
        lista = self.inimigo.falas.get(situacao, [])
        if lista:
            fala = random.choice(lista)
            ui.console.print(f"\n[bold red]{self.inimigo.nome}:[/bold red] {fala}")

    def iniciar_combate(self):
        ui.limpar_tela()
        ui.console.print(f"\n[bold red]Um perigo se aproxima no horizonte...[/bold red]")
        
        # Mapeamento de imagens
        old_folder = r"C:\Users\vinic\.gemini\antigravity\brain\e6a79699-bf18-4c87-982a-2d49a9e99e21"
        new_folder = r"C:\Users\vinic\.gemini\antigravity\brain\1149e488-93d8-4b3b-ad9d-70e9dd074eee"
        
        enemy_imgs = {
            "Coiote Faminto": (old_folder, "lobo_coiote_1778027475322.png"),
            "Lobo Pequeno": (old_folder, "lobo_coiote_1778027475322.png"),
            "Urso Cinzento das Montanhas": (new_folder, "urso_cinzento_1779226147184.png"),
            "Abutre Faminto": (old_folder, "abutre_1778027551924.png"),
            "Bêbado do Saloon": (new_folder, "bebado_saloon_1779226159845.png"),
            "Guarda do Trem": (new_folder, "guarda_trem_1779226279482.png"),
            "Desertor da Cavalaria": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "O Coronel Sem Nome": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "Garimpeiro Ganancioso": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "Capataz da Fazenda": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "O Carrasco de Black Rock": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "Pistoleiro de Aluguel": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "Caçador de Recompensas Rival": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "Billy the Kid": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "Xerife Corrupto": (old_folder, "ladrao_bandoleiro_1778028056322.png"),
            "Xerife Renegado": (old_folder, "ladrao_bandoleiro_1778028056322.png")
        }
        
        folder, img_name = enemy_imgs.get(self.inimigo.nome, (old_folder, "ladrao_bandoleiro_1778028056322.png"))
        img_path = f"{folder}\\{img_name}"
        ui.mostrar_imagem(img_path)
        
        ui.esperar_enter()

        if self.inimigo.historia:
            ui.console.print(f"\n[italic gray]*{self.inimigo.historia}*[/italic gray]")
            ui.esperar_enter()

        ui.limpar_tela()
        self.mostrar_fala_inimigo("inicio")
        ui.esperar_enter()

        while self.jogador.vida_atual > 0 and self.inimigo.vida_atual > 0:
            ui.limpar_tela()
            ui.exibir_combate(self.jogador, self.inimigo)

            ui.console.print("\n[bold]O que você deseja fazer?[/bold]")
            opcoes_combate = {
                "⚔️ Atacar": "1",
                "🛡️ Defender": "2",
                "🎒 Usar Item": "3",
                "🏃 Fugir": "4"
            }
            escolha = ui.receber_escolha("", opcoes_combate)

            defesa_bonus_jogador = 0
            fugiu = False

            # Turno do Jogador
            if escolha == "1":
                if self.jogador.muniçao > 0:
                    self.jogador.muniçao -= 1
                    dano = self.calcular_dano(self.jogador, self.inimigo)
                    if dano > 0:
                        ui.console.print(f"\n[bold green]Você acertou o {self.inimigo.nome} e causou {dano} de dano![/bold green]")
                        self.inimigo.receber_dano(dano)
                        self.mostrar_fala_inimigo("levou_tiro")
                    else:
                        ui.console.print(f"\n[bold yellow]Você errou o tiro![/bold yellow]")
                        self.mostrar_fala_inimigo("jogador_errou")
                else:
                    ui.console.print("[bold red]Você está sem munição! Perdeu o turno tentando atirar.[/bold red]")

            elif escolha == "2":
                defesa_bonus_jogador = self.jogador.defesa // 2
                ui.console.print(f"[bold blue]Você se prepara para o impacto. Defesa aumentada em {defesa_bonus_jogador} para este turno.[/bold blue]")

            elif escolha == "3":
                itens_usaveis = [item for item, qtd in self.jogador.inventario.items() if qtd > 0 and item in ["Bandagem", "Uísque", "Dinamite"]]
                if not itens_usaveis:
                    ui.console.print("[bold red]Você não tem itens úteis para usar agora![/bold red]")
                else:
                    ui.console.print("\n[bold]Qual item deseja usar?[/bold]")
                    opcoes_itens = {f"{item} ({self.jogador.inventario[item]}x)": str(i+1) for i, item in enumerate(itens_usaveis)}
                    opcoes_itens["❌ Voltar"] = "0"
                    
                    escolha_item = ui.receber_escolha("", opcoes_itens)
                    try:
                        idx = int(escolha_item) - 1
                        if idx >= 0 and idx < len(itens_usaveis):
                            item_escolhido = itens_usaveis[idx]
                            resultado = self.jogador.usar_item(item_escolhido)
                            
                            if resultado["tipo"] == "cura":
                                ui.console.print(f"[bold green]{resultado['msg']}[/bold green]")
                            elif resultado["tipo"] == "dano_inimigo":
                                ui.console.print(f"[bold yellow]{resultado['msg']}[/bold yellow]")
                                self.inimigo.receber_dano(resultado["valor"])
                            else:
                                ui.console.print(f"[bold red]{resultado['msg']}[/bold red]")
                        else:
                            ui.console.print("[yellow]Ação cancelada.[/yellow]")
                            continue # Volta pro menu sem gastar turno
                    except ValueError:
                        ui.console.print("[red]Opção inválida![/red]")
                        continue

            elif escolha == "4":
                if random.random() < 0.4:  # 40% de chance de fugir
                    ui.console.print(f"\n[bold cyan]Você conseguiu fugir com sucesso![/bold cyan]")
                    time.sleep(2)
                    fugiu = True
                    break
                else:
                    ui.console.print(f"\n[bold red]Você tentou fugir, mas o inimigo te bloqueou![/bold red]")
                    self.mostrar_fala_inimigo("inicio")

            else:
                ui.console.print(f"\n[bold red]Ação inválida! Você perdeu o turno.[/bold red]")

            time.sleep(1.5)

            if self.inimigo.vida_atual <= 0:
                ui.limpar_tela()
                ui.console.print(f"\n[bold green]Vitória! Você derrotou o {self.inimigo.nome}.[/bold green]")
                self.mostrar_fala_inimigo("morte")
                self.jogador.ganhar_exp(self.inimigo.exp_recompensa)
                time.sleep(2)
                break

            # Turno do Inimigo
            ui.console.print(f"\n[italic]Turno do {self.inimigo.nome}...[/italic]")
            time.sleep(1)
            
            dano_inimigo = self.calcular_dano(
                self.inimigo, self.jogador, defesa_bonus_jogador)

            if dano_inimigo > 0:
                ui.console.print(f"[bold red]O {self.inimigo.nome} te atacou e causou {dano_inimigo} de dano![/bold red]")
                self.jogador.receber_dano(dano_inimigo)
                self.mostrar_fala_inimigo("acertou")
            else:
                ui.console.print(f"[bold yellow]O {self.inimigo.nome} errou o ataque![/bold yellow]")
                self.mostrar_fala_inimigo("errou")

            time.sleep(2)

            if self.jogador.vida_atual <= 0:
                ui.limpar_tela()
                ui.console.print("\n[bold red]Você foi derrotado... O deserto não perdoa os fracos.[/bold red]")
                time.sleep(2)
                return False  # Fim de jogo

        return True  # Combate terminou (vitória ou fuga)

    # Cálculo do dano
    def calcular_dano(self, atacante, defensor, bonus_defesa=0):

        # Lógica de acerto baseada em D20 vs Esquiva
        rolagem = self.dados.rolar_d20()

        if rolagem >= defensor.esquiva:

            # Dano = (Poder + D6) - (Defesa + bonus)
            dano_base = atacante.poder + self.dados.rolar_d6()
            defesa_total = defensor.defesa + bonus_defesa

            dano_final = dano_base - defesa_total

            # Retorna o maior valor entre 1 e o dano se acertar
            return max(1, dano_final)

        return 0  # Errou
