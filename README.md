# Golden Rock - RPG de Faroeste 

##  Sobre o Jogo
O **Golden Rock** é um jogo de RPG baseado em texto com uma interface gráfica personalizada (utilizando `tkinter`), ambientado no impiedoso Velho Oeste. Assuma o papel de um aventureiro, escolha a sua classe e vocação, e desbrave os perigos do deserto, enfrentando bandoleiros, xerifes corruptos e feras selvagens.

##  Funcionalidades
* **Criação de Personagem:** Escolha um nome, uma Classe e uma Vocação, cada uma com atributos únicos (Poder, Defesa, Vida, Munição e Itens iniciais).
* **Interface Gráfica Interativa:** O jogo utiliza uma interface gráfica rica (`ui.py`) para simular uma consola imersiva, apresentando imagens dinâmicas e texto formatado e colorido.
* **Sistema de Exploração (D20):** Aventure-se pelo mapa rolando um dado de 20 faces. O resultado da sua rolagem determina se encontra eventos especiais (como baús e assaltos a comboios), abrigos seguros ou se sofre emboscadas.
* **Combate por Turnos:** Enfrente inimigos variados utilizando um sistema estratégico onde pode:
    * **Atacar:** Utiliza o seu poder de fogo, consumindo munição.
    * **Defender:** Aumenta temporariamente a sua defesa para mitigar o dano inimigo.
    * **Usar Itens:** Aceda à sua sela para utilizar Bandagens, Uísque ou Dinamite.
    * **Fugir:** Tente escapar com base numa probabilidade de sucesso.
* **Progressão Constante:** Ganhe pontos de experiência (EXP) ao derrotar adversários e suba de nível para melhorar os seus atributos e restaurar a sua saúde.

##  Pré-requisitos
Para executar o jogo corretamente, necessitará do **Python 3.x** instalado no seu sistema, bem como a biblioteca para processamento de imagens.

##  Como Executar

1.  Abra o terminal ou a linha de comandos na diretoria raiz do projeto.
2.  Instale a dependência necessária executando o seguinte comando:
    ```bash
    pip install pillow
    ```
3.  Inicie o jogo executando o ficheiro principal:
    ```bash
    python main.py
    ```

##  Estrutura do Projeto
* `main.py`: Ponto de entrada do jogo. Gere o menu principal e o fluxo principal do jogador.
* `ui.py`: Responsável pela interface gráfica, captura de eventos do teclado e renderização de ecrãs e imagens.
* `entidades/`: Contém as definições de vida e comportamento das personagens (`jogador.py`, `inimigo.py`, `entidade.py`).
* `combate/`: Lógica do sistema de embates por turnos e cálculo de dano (`combate.py`).
* `sistema_dados/`: Sistema de rolagem de dados virtuais para o RPG.
* `eventos/`: Ficheiros para os eventos aleatórios de exploração (assalto ao comboio, eventos de baú).
* `classes_jogador/` & `vocacoes/`: Definições das estatísticas base das diferentes origens que o jogador pode escolher.
* `assets/`: Diretoria onde se encontram todas as imagens do jogo em formato `.png`.

##  Inventário e Itens
Ao longo da sua jornada, poderá utilizar os itens guardados na sua sela:
* **Bandagem:** Cura 20 pontos de Vida (HP).
* **Uísque:** Restaura 40 pontos de Vida (HP) com um bom gole de vigor.
* **Dinamite:** Causa 25 pontos de dano direto e explosivo ao inimigo num combate.

---
*Engraxe as suas botas e prepare o revólver. A sua história no deserto começa agora!*
