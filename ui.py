import os
import time
import tkinter as tk
import threading
import re
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Golden Rock - RPG")
        self.root.geometry("800x650")
        self.root.configure(bg="#121212")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.text_widget = tk.Text(self.root, bg="#121212", fg="#e0e0e0", 
                                   font=("Consolas", 14), wrap="word", state=tk.DISABLED,
                                   insertbackground="white", borderwidth=0, highlightthickness=0)
        self.text_widget.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.text_widget.tag_configure("red", foreground="#ff4c4c")
        self.text_widget.tag_configure("green", foreground="#4caf50")
        self.text_widget.tag_configure("yellow", foreground="#ffeb3b")
        self.text_widget.tag_configure("cyan", foreground="#00bcd4")
        self.text_widget.tag_configure("blue", foreground="#2196f3")
        self.text_widget.tag_configure("gray", foreground="#9e9e9e")
        self.text_widget.tag_configure("magenta", foreground="#e91e63")
        self.text_widget.tag_configure("white", foreground="#ffffff")
        self.text_widget.tag_configure("bold", font=("Consolas", 14, "bold"))
        self.text_widget.tag_configure("italic", font=("Consolas", 14, "italic"))
        self.text_widget.tag_configure("center", justify="center")
        
        self.entry = tk.Entry(self.root, bg="#2d2d2d", fg="white", font=("Consolas", 16), borderwidth=0)
        self.entry.pack(fill="x", padx=20, pady=(0, 20), ipady=5)
        
        self.entry.bind("<Return>", self.on_enter)
        self.root.bind("<space>", self.on_space)
        self.root.bind("<Return>", self.on_space)
        
        self.input_event = threading.Event()
        self.user_input = ""
        self.waiting_for_continue = False
        self.images = []

    def show_buttons(self, options):
        self.entry.pack_forget()
        
        if hasattr(self, 'button_frame'):
            self.button_frame.destroy()
            
        self.button_frame = tk.Frame(self.root, bg="#121212")
        self.button_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        if isinstance(options, list):
            options = {v: str(i+1) for i, v in enumerate(options)}
            
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        
        for i, (option_text, option_value) in enumerate(options.items()):
            btn = tk.Button(self.button_frame, text=option_text, bg="#2d2d2d", fg="white", 
                            font=("Consolas", 12), command=lambda v=option_value: self.on_button_click(v),
                            activebackground="#4caf50", activeforeground="white", borderwidth=1, relief="solid",
                            wraplength=350)
            btn.grid(row=i//2, column=i%2, sticky="ew", padx=5, pady=5)
            
    def on_button_click(self, value):
        self.user_input = str(value)
        self.button_frame.destroy()
        self.entry.pack(fill="x", padx=20, pady=(0, 20), ipady=5)
        self.entry.focus()
        self.input_event.set()

    def on_closing(self):
        os._exit(0)
        
    def on_enter(self, event):
        if self.waiting_for_continue:
            self.waiting_for_continue = False
            self.input_event.set()
        else:
            self.user_input = self.entry.get()
            self.entry.delete(0, tk.END)
            self.input_event.set()

    def on_space(self, event):
        if self.waiting_for_continue:
            self.waiting_for_continue = False
            self.input_event.set()
            
    def start(self):
        self.root.mainloop()

gui = GameGUI()

class ConsoleMock:
    def print(self, text="", style=None, justify=None):
        tags = []
        if style:
            tags.extend(style.split())
        if justify == "center":
            tags.append("center")
            
        parts = re.split(r'(\[.*?\])', str(text))
        active_tags = list(tags)
        
        gui.text_widget.config(state=tk.NORMAL)
        for part in parts:
            if part.startswith('[') and part.endswith(']'):
                tag = part[1:-1]
                if tag.startswith('/'):
                    tag_name = tag[1:]
                    if tag == "/":
                        active_tags = list(tags)
                    elif " " in tag_name:
                        for sub in tag_name.split():
                            if sub in active_tags:
                                active_tags.remove(sub)
                    else:
                        if tag_name in active_tags:
                            active_tags.remove(tag_name)
                else:
                    for sub in tag.split():
                        active_tags.append(sub)
            else:
                if part:
                    gui.text_widget.insert(tk.END, part, tuple(active_tags))
        gui.text_widget.insert(tk.END, "\n")
        gui.text_widget.see(tk.END)
        gui.text_widget.config(state=tk.DISABLED)

console = ConsoleMock()

def limpar_tela():
    gui.text_widget.config(state=tk.NORMAL)
    gui.text_widget.delete('1.0', tk.END)
    gui.text_widget.config(state=tk.DISABLED)

def imprimir_lento(texto, cor="white", atraso=0.015):
    gui.text_widget.config(state=tk.NORMAL)
    for char in texto:
        gui.text_widget.insert(tk.END, char, (cor,))
        gui.text_widget.see(tk.END)
        gui.root.update()
        time.sleep(atraso)
    gui.text_widget.insert(tk.END, "\n")
    gui.text_widget.config(state=tk.DISABLED)

def tela_titulo():
    limpar_tela()
    img_path = os.path.join(BASE_DIR, "assets", "faroeste_capa_1778027339569.png")
    if os.path.exists(img_path):
        mostrar_imagem(img_path, width=400, height=300)
    
    console.print("🌵 BEM VINDO A GOLDEN ROCK! 🌵", style="bold yellow", justify="center")
    console.print("-" * 40, style="yellow", justify="center")
    time.sleep(1)

def mostrar_cabecalho(jogador):
    vida_pct = (jogador.vida_atual / jogador.vida_maxima) * 100
    cor_vida = "green" if vida_pct > 50 else "yellow" if vida_pct > 20 else "red"
    
    info = f"🤠 [bold yellow]{jogador.nome}[/bold yellow] | 🎖️ Nível: [cyan]{jogador.nivel}[/cyan] | ❤️ HP: [{cor_vida}]{jogador.vida_atual}/{jogador.vida_maxima}[/{cor_vida}] | 🔫 Munição: [white]{jogador.muniçao}[/white]"
    console.print(info, justify="center")
    console.print("-" * 60, style="blue", justify="center")

def mostrar_menu_principal():
    console.print("\n[bold]O que você vai fazer, parceiro?[/bold]", justify="center")
    console.print("[bold green][1][/bold green] - 🏇 Viajar (Inicia combate)")
    console.print("[bold green][2][/bold green] - 🌍 Explorar (Eventos e descobertas)")
    console.print("[bold green][3][/bold green] - 🎒 Conferir Sela (Inventário e Status)")
    console.print("[bold green][4][/bold green] - 🚪 Sair do Jogo")

def mostrar_imagem(caminho, width=300, height=300):
    try:
        img = Image.open(caminho)
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        gui.images.append(photo)
        
        gui.text_widget.config(state=tk.NORMAL)
        gui.text_widget.image_create(tk.END, image=photo, align="center")
        gui.text_widget.insert(tk.END, "\n")
        gui.text_widget.see(tk.END)
        gui.text_widget.config(state=tk.DISABLED)
    except Exception as e:
        console.print(f"[red]Erro ao carregar imagem: {e}[/red]")

def mostrar_inventario(jogador):
    limpar_tela()
    console.print(f"[bold yellow]--- Sela de {jogador.nome} ---[/bold yellow]", justify="center")
    
    # Ilustração da Sela
    img_path = os.path.join(BASE_DIR, "assets", "sela_faroeste_1778026536324.png")
    if os.path.exists(img_path):
        mostrar_imagem(img_path)
    
    console.print(f"[cyan]Classe:[/cyan] {jogador.raca} | [cyan]Vocação:[/cyan] {jogador.vocacao}")
    console.print(f"[cyan]Nível:[/cyan] {jogador.nivel} (EXP: {jogador.exp}/{jogador.nivel*100})")
    console.print(f"[cyan]Munição:[/cyan] {jogador.muniçao} | [cyan]Poder:[/cyan] {jogador.poder} | [cyan]Defesa:[/cyan] {jogador.defesa}")
    
    console.print("\n[bold green]--- Itens na Sela ---[/bold green]")
    for item, qtd in jogador.inventario.items():
        console.print(f"[magenta]{item}[/magenta]: {qtd}")
    console.print()

def mensagem_evento(titulo, texto, cor="cyan"):
    console.print(f"\n[bold {cor}]--- {titulo} ---[/bold {cor}]")
    console.print(texto)
    console.print("-" * 40, style=cor)

def barra_de_vida(nome, atual, maxima, cor):
    tamanho = 20
    if maxima <= 0: maxima = 1
    preenchido = int((atual / maxima) * tamanho)
    if preenchido < 0: preenchido = 0
    if preenchido > tamanho: preenchido = tamanho
    vazio = tamanho - preenchido
    barra = f"[{cor}]{'█' * preenchido}[/{cor}][gray]{'░' * vazio}[/gray]"
    return f"{nome: <15} {barra} {atual}/{maxima}"

def exibir_combate(jogador, inimigo):
    console.print("[bold red]⚔️  EMBATE FEROZ ⚔️[/bold red]", justify="center")
    console.print("="*60, style="red", justify="center")
    
    vida_jog = barra_de_vida(jogador.nome, jogador.vida_atual, jogador.vida_maxima, "green")
    vida_ini = barra_de_vida(inimigo.nome, inimigo.vida_atual, inimigo.vida_maxima, "red")
    
    console.print(vida_jog)
    console.print(f"[blue]Munição:[/blue] {jogador.muniçao}")
    console.print("")
    console.print(vida_ini)
    console.print(f"[bold yellow]{inimigo.dificuldade.upper()}[/bold yellow]\n")

# Substituir o input nativo pelo da interface gráfica
def receber_input(prompt=""):
    if prompt:
        console.print(f"[bold cyan]{prompt}[/bold cyan]")
    gui.waiting_for_continue = False
    gui.input_event.clear()
    gui.entry.focus()
    gui.input_event.wait()
    return gui.user_input

def receber_escolha(prompt, opcoes_dict):
    if prompt:
        console.print(f"[bold cyan]{prompt}[/bold cyan]")
    gui.waiting_for_continue = False
    gui.input_event.clear()
    gui.show_buttons(opcoes_dict)
    gui.input_event.wait()
    return gui.user_input

def esperar_enter():
    console.print("\n[italic gray][ Pressione ENTER ou ESPAÇO para avançar ][/italic gray]", justify="center")
    gui.waiting_for_continue = True
    gui.input_event.clear()
    gui.entry.delete(0, tk.END)
    gui.root.focus()
    gui.input_event.wait()
