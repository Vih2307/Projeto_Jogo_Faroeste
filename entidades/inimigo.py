from entidades.entidade import Entidade


class Inimigo(Entidade):
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, vida_atual: int, esquiva: int, exp_recompensa: int, dificuldade: str, historia: str, falas: dict):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.exp_recompensa = exp_recompensa
        self.dificuldade = dificuldade
        self.historia = historia
        self.falas = falas


Inimigos = {
    # Nivel Facil
    "Coiote Faminto": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50,

        "historia": (
            "Um coiote magro que ronda as trilhas de Golden Rock. "
            "Dizem que ele aprendeu a seguir viajantes feridos e atacar ao anoitecer."
        ),

        "falas": {
            "inicio": [
                "O coiote rosna e circula você com fome nos olhos.",
                "O animal fareja o ar, como se já sentisse o cheiro do seu sangue."
            ],
            "levou_tiro": [
                "O coiote solta um ganido feroz e recua cambaleando.",
                "A bala rasga o couro do animal, que rosna com ainda mais raiva."
            ],
            "jogador_errou": [
                "O coiote desvia num salto rápido pela areia.",
                "Seu tiro levanta poeira, mas o bicho continua avançando."
            ],
            "acertou": [
                "O coiote avança e morde sua perna com violência.",
                "Num bote rápido, o animal te acerta antes que você recue."
            ],
            "errou": [
                "O coiote tenta pular em você, mas passa raspando.",
                "As presas estalam no vazio. Por pouco."
            ],
            "morte": [
                "O coiote cai na areia e solta um último rosnado.",
                "Ferido demais para continuar, o animal desaba no chão seco."
            ]
        }
    },
    "Lobo Pequeno": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50,

        "historia": (
            "Um jovem lobo separado da alcateia. Ainda inexperiente, mas já aprendeu que a fome "
            "é mais perigosa que qualquer caçador."
        ),
        "falas": {
            "inicio": ["O lobo rosna baixo, observando seus movimentos."],
            "levou_tiro": ["O lobo uiva de dor e recua."],
            "jogador_errou": ["O lobo desvia rapidamente pelo deserto."],
            "acertou": ["O lobo avança e morde com ferocidade."],
            "errou": ["O lobo salta, mas erra o ataque."],
            "morte": ["O lobo cai e solta um último uivo."]
        }

    },

    "Ladrão de Galinhas": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50,

        "historia": (
            "Um ladrãozinho oportunista que sobrevive roubando de fazendas. "
            "Não é perigoso... até ser encurralado."
        ),
        "falas": {
            "inicio": ["Ei! Eu não fiz nada, parceiro... não precisa disso!"],
            "levou_tiro": ["Droga! Tá maluco?!"],
            "jogador_errou": ["Haha! Nem sabe atirar direito!"],
            "acertou": ["Fica quieto e entrega tudo!"],
            "errou": ["Maldição... fica parado!"],
            "morte": ["Eu só queria sobreviver..."]
        }
    },
    "Bêbado do Saloon": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50,

        "historia": (
            "Um homem perdido no álcool e nas próprias escolhas. Vive arrumando briga "
            "sem nem lembrar o motivo."
        ),
        "falas": {
            "inicio": ["Ocê... tá me encarando, amigo?"],
            "levou_tiro": ["Ei... isso doeu mais do que parece..."],
            "jogador_errou": ["Haha... até bêbado eu sou mais rápido!"],
            "acertou": ["Toma isso... hic!"],
            "errou": ["Droga... onde você foi parar...?"],
            "morte": ["Heh... acho que bebi demais dessa vez..."]
        }
    },
    "Abutre Faminto": {
        "poder": 5,
        "defesa": 2,
        "vida": 20,
        "esquiva": 10,
        "dificuldade": "Facil",
        "exp_recompensa": 50,

        "historia": (
            "Um abutre que já não espera mais a morte chegar. "
            "Ele mesmo decide quando é hora da presa cair."
        ),
        "falas": {
            "inicio": ["O abutre circula no alto antes de mergulhar."],
            "levou_tiro": ["O abutre grita e bate as asas descontrolado."],
            "jogador_errou": ["O abutre sobe rapidamente evitando o tiro."],
            "acertou": ["As garras rasgam sua carne."],
            "errou": ["O ataque passa raspando."],
            "morte": ["O abutre cai do céu sem vida."]
        }
    },
    # Nivel Medio
    "Guarda do Trem": {
        "poder": 12,
        "defesa": 6,
        "vida": 45,
        "esquiva": 10,
        "dificuldade": "Médio",
        "exp_recompensa": 120,
        "historia": (
            "Um segurança contratado para proteger cargas valiosas nas ferrovias do oeste."
        ),
        "falas": {
            "inicio": [
                "Ninguém rouba este trem enquanto eu estiver de pé.",
                "Desça desse vagão, forasteiro."
            ],
            "levou_tiro": [
                "Droga! Você vai pagar por isso!",
                "Maldito pistoleiro!"
            ],
            "jogador_errou": [
                "Mira ruim pra um ladrão de trem.",
                "Vai precisar de mais do que isso."
            ],
            "acertou": [
                "Fim da linha pra você!",
                "Esse vagão será seu túmulo!"
            ],
            "errou": [
                "Fique parado!",
                "Você teve sorte!"
            ],
            "morte": [
                "O trem... precisa seguir...",
                "Você... não devia estar aqui..."
            ]
        }
    },
    "Ladrao de Gado": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100,

        "historia": (
            "Um especialista em desaparecer com rebanhos durante a noite. "
            "Conhece atalhos que nem os donos das terras conhecem."
        ),
        "falas": {
            "inicio": ["Essas terras não têm dono... agora são minhas."],
            "levou_tiro": ["Você vai pagar por esse tiro!"],
            "jogador_errou": ["Mira pior que de fazendeiro velho!"],
            "acertou": ["O gado não foi a única coisa que eu roubei hoje!"],
            "errou": ["Droga! Você escapou por pouco!"],
            "morte": ["Maldição... perdi tudo..."]
        }
    },
    "Bandoleiro de Estrada": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100,

        "historia": (
            "Um fora-da-lei que vive de emboscadas. Sua fama corre mais rápido que seu cavalo."
        ),
        "falas": {
            "inicio": ["Pare aí mesmo... ou vai se arrepender."],
            "levou_tiro": ["Então quer brincar de duelo?!"],
            "jogador_errou": ["Esse foi seu melhor tiro?"],
            "acertou": ["Bem-vindo à estrada errada, amigo."],
            "errou": ["Você não vai ter tanta sorte de novo."],
            "morte": ["A estrada... venceu dessa vez..."]
        }
    },
    "Garimpeiro Ganancioso": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100,

        "historia": (
            "Um homem consumido pela busca por ouro. Agora vê riqueza em qualquer um que cruza seu caminho."
        ),
        "falas": {
            "inicio": ["Eu sei que você tá escondendo ouro..."],
            "levou_tiro": ["Você não vai levar minha fortuna!"],
            "jogador_errou": ["Haha! Nem pra isso você serve!"],
            "acertou": ["Tudo que você tem agora é meu!"],
            "errou": ["Droga! Eu preciso disso!"],
            "morte": ["Meu ouro... meu ouro..."]
        }
    },
    "Capataz da Fazenda": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100,

        "historia": (
            "Um homem endurecido pela vida no campo. Governa com medo e força."
        ),
        "falas": {
            "inicio": ["Aqui quem manda sou eu."],
            "levou_tiro": ["Você acabou de cavar sua cova."],
            "jogador_errou": ["Fraco demais pra trabalhar..."],
            "acertou": ["Aprenda a respeitar autoridade."],
            "errou": ["Fica parado!"],
            "morte": ["A fazenda... precisa de mim..."]
        }
    },
    "Desertor da Cavalaria": {
        "poder": 10,
        "defesa": 5,
        "vida": 40,
        "esquiva": 8,
        "dificuldade": "Médio",
        "exp_recompensa": 100,

        "historia": (
            "Um soldado que abandonou tudo. Vive com medo de ser reconhecido — e elimina qualquer ameaça."
        ),
        "falas": {
            "inicio": ["Você não viu nada... entendeu?"],
            "levou_tiro": ["Droga! Eles te mandaram?!"],
            "jogador_errou": ["Você não é soldado coisa nenhuma."],
            "acertou": ["Ninguém vai me levar de volta!"],
            "errou": ["Maldição!"],
            "morte": ["Eu... só queria fugir..."]
        }
    },
    # Nivel Dificil
    "Pistoleiro de Aluguel": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200,

        "historia": (
            "Um assassino profissional. Cada tiro seu tem preço — e quase nunca erra."
        ),
        "falas": {
            "inicio": ["Nada pessoal... só negócios."],
            "levou_tiro": ["Interessante... você é rápido."],
            "jogador_errou": ["Erro fatal."],
            "acertou": ["Contrato concluído."],
            "errou": ["Quase..."],
            "morte": ["Heh... bom duelo..."]
        }
    },
    "Assaltante de Trem": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200,

        "historia": (
            "Especialista em grandes golpes. Já roubou mais ouro do que muitos já viram na vida."
        ),
        "falas": {
            "inicio": ["Esse trem já foi meu... agora é você."],
            "levou_tiro": ["Você não sabe com quem mexeu!"],
            "jogador_errou": ["Haha! Muito lento!"],
            "acertou": ["Isso aqui é um assalto!"],
            "errou": ["Fica parado!"],
            "morte": ["O ouro... ficou pra trás..."]
        }
    },
    "Xerife Corrupto": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200,

        "historia": (
            "A lei virou apenas uma desculpa para dominar. Ele decide quem vive... e quem morre."
        ),
        "falas": {
            "inicio": ["A lei sou eu."],
            "levou_tiro": ["Você ousa atirar em um xerife?!"],
            "jogador_errou": ["Patético."],
            "acertou": ["Sentença cumprida."],
            "errou": ["Você teve sorte."],
            "morte": ["A lei... falhou..."]
        }
    },
    "Urso Cinzento das Montanhas": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200,

        "historia": (
            "Uma força da natureza. Não caça por maldade — apenas protege seu território."
        ),
        "falas": {
            "inicio": ["*O urso ruge e bate no chão.*"],
            "levou_tiro": ["*O rugido ecoa pela montanha.*"],
            "jogador_errou": ["*O urso avança ignorando o tiro.*"],
            "acertou": ["*Uma pancada devastadora te atinge.*"],
            "errou": ["*O ataque erra por pouco.*"],
            "morte": ["*O gigante cai lentamente.*"]
        }
    },
    "Caçador de Recompensas Rival": {
        "poder": 18,
        "defesa": 12,
        "vida": 85,
        "esquiva": 15,
        "dificuldade": "Difícil",
        "exp_recompensa": 200,

        "historia": (
            "Um rival direto. Para ele, você é apenas mais um prêmio."
        ),
        "falas": {
            "inicio": ["Nada pessoal... só quero a recompensa."],
            "levou_tiro": ["Você é melhor do que pensei."],
            "jogador_errou": ["Amador."],
            "acertou": ["Fim da linha."],
            "errou": ["Quase..."],
            "morte": ["Droga... você ganhou..."]
        }
    },
    # Nivel Chefe
    "Xerife Renegado": {
        "poder": 30,
        "defesa": 20,
        "vida": 250,
        "esquiva": 20,
        "dificuldade": "Chefe",
        "exp_recompensa": 500,

        "historia": (
            "Traído pela própria cidade, agora busca vingança contra todos."
        ),
        "falas": {
            "inicio": ["Todos vão pagar."],
            "levou_tiro": ["Você não entende o que fizeram comigo!"],
            "jogador_errou": ["Fraco."],
            "acertou": ["Isso é justiça."],
            "errou": ["Você não vai escapar."],
            "morte": ["Talvez... eu estivesse errado..."]
        }
    },
    "O Coronel Sem Nome": {
        "poder": 30,
        "defesa": 20,
        "vida": 250,
        "esquiva": 20,
        "dificuldade": "Chefe",
        "exp_recompensa": 500,

        "historia": (
            "Um fantasma da guerra. Seu passado foi apagado — mas sua habilidade não."
        ),
        "falas": {
            "inicio": ["Soldado... você não deveria estar aqui."],
            "levou_tiro": ["Bom tiro."],
            "jogador_errou": ["Treine mais."],
            "acertou": ["Alvo eliminado."],
            "errou": ["Ajustando mira..."],
            "morte": ["Missão... falhou..."]
        }
    },
    "O Carrasco de Black Rock": {
        "poder": 30,
        "defesa": 20,
        "vida": 250,
        "esquiva": 20,
        "dificuldade": "Chefe",
        "exp_recompensa": 500,

        "historia": (
            "Um executor cruel que acredita estar fazendo justiça."
        ),
        "falas": {
            "inicio": ["Sua sentença já foi decidida."],
            "levou_tiro": ["Você não foge do destino."],
            "jogador_errou": ["Inevitável."],
            "acertou": ["Execução em andamento."],
            "errou": ["Prolongando o sofrimento..."],
            "morte": ["O carrasco... caiu..."]
        }
    },
    "Billy the Kid": {
        "poder": 30,
        "defesa": 20,
        "vida": 250,
        "esquiva": 20,
        "dificuldade": "Chefe",
        "exp_recompensa": 500,

        "historia": (
            "Uma lenda viva. Rápido, imprevisível e mortal."
        ),
        "falas": {
            "inicio": ["Vamos ver quem é mais rápido."],
            "levou_tiro": ["Heh... gostei disso."],
            "jogador_errou": ["Muito lento."],
            "acertou": ["Esse foi bonito."],
            "errou": ["Quase pegou."],
            "morte": ["Heh... bom duelo... parceiro..."]
        }
    },

}
