import random
import ui
from entidades.jogador import Jogador
from sistema_dados.dados import SistemaDados


def evento_bau(jogador, dados):
    ui.mensagem_evento("Baú Misterioso", "Você encontrou um baú antigo enterrado na areia!\nVocê terá 3 tentativas para abri-lo. Precisa tirar 10 ou mais no D20.", "yellow")

    bau_aberto = False

    for tentativa in range(1, 4):
        ui.esperar_enter()
        rolagem_bau = dados.rolar_d20()
        ui.console.print(f"Tentativa {tentativa}: você tirou [bold cyan]{rolagem_bau}[/bold cyan] no dado.")

        if rolagem_bau >= 10:
            ui.console.print("\n[bold green]Você conseguiu abrir o baú![/bold green]")
            ui.console.print("Dentro dele havia [yellow]+12 Munição[/yellow] e [yellow]+2 Bandagens[/yellow] e [yellow]+1 Dinamite[/yellow]!")
            jogador.muniçao += 12
            jogador.inventario["Bandagem"] = jogador.inventario.get("Bandagem", 0) + 2
            jogador.inventario["Dinamite"] = jogador.inventario.get("Dinamite", 0) + 1
            bau_aberto = True
            break
        else:
            ui.console.print("[red]A fechadura não abriu...[/red]")

    if not bau_aberto:
        ui.console.print("\n[bold gray]Depois de 3 tentativas, você não conseguiu abrir o baú.[/bold gray]")
        ui.console.print("[italic]Talvez precise de mais sorte na próxima vez.[/italic]")
    return True
