from entidades.entidade import Entidade


class Jogador(Entidade):
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, vida_atual: int, esquiva: int, muniçao: int, nivel: int, exp: int, raca: str, vocacao: str, inventario: dict):
        super().__init__(nome, poder, defesa, vida_maxima, vida_atual, esquiva)
        self.muniçao = muniçao
        self.nivel = nivel
        self.exp = exp
        self.raca = raca
        self.vocacao = vocacao
        self.inventario = inventario

    def ganhar_exp(self, quantidade):
        self.exp += quantidade
        print(
            f"\n{self.nome} ganhou {quantidade} de EXP e agora está com {self.exp} de EXP!!")
        self.subir_nivel()

    def subir_nivel(self, ):
        # Para subir de nível, temos que ganhar 100 * o nível atual, ou seja 100 EXP para ir para o nível 2 e 200 de EXP para o nível 3
        exp_necessaria = self.nivel * 100

        while self.exp >= exp_necessaria:
            self.exp -= exp_necessaria
            self.nivel += 1
            self.poder += 2
            self.defesa += 1
            self.vida_maxima += 5
            self.vida_atual = self.vida_maxima
            print(
                f"{self.nome} subiu para o nível {self.nivel}!! Atributos aumentados e vida restaurada.")
            exp_necessaria = self.nivel * 100

    def usar_item(self, item_nome):
        if item_nome in self.inventario and self.inventario[item_nome] > 0:
            if item_nome == "Bandagem":
                self.curar(20)
                self.inventario[item_nome] -= 1
                return {"tipo": "cura", "valor": 20, "msg": f"Você usou uma Bandagem e curou 20 de HP! (Restam {self.inventario[item_nome]})"}
            elif item_nome == "Uísque":
                self.curar(40)
                self.inventario[item_nome] -= 1
                return {"tipo": "cura", "valor": 40, "msg": f"Você deu um gole no Uísque e sentiu o vigor voltar! +40 HP (Restam {self.inventario[item_nome]})"}
            elif item_nome == "Dinamite":
                self.inventario[item_nome] -= 1
                return {"tipo": "dano_inimigo", "valor": 25, "msg": f"Você acendeu a Dinamite e jogou! KABOOM! 25 de Dano! (Restam {self.inventario[item_nome]})"}
            else:
                return {"tipo": "erro", "msg": f"Você não sabe como usar {item_nome} ou não pode usá-lo agora."}
        else:
            return {"tipo": "erro", "msg": f"Você não tem {item_nome} no inventário."}


# CLASSES_FAROESTE = {
#     "Indígena":      {"poder": 5, "defesa": 7, "vida": 20, "muniçao": 6},
#     "Caçador de Recompensa":  {"poder": 8, "defesa": 2, "vida": 25, "muniçao": 20},
#     "Veterano de Guerra":    {"poder": 10, "defesa": 5, "vida": 15, "muniçao": 12}
# }

# VOCAÇÕES_FAROESTE = {
#     "Pistoleiro":  {"poder": 8, "defesa": 1, "vida": 5, "muniçao": 12, "item": "Revólver"},
#     "Rastreador":      {"poder": 2, "defesa": 10, "vida": 4, "muniçao": 3, "item": "Escopeta"},
#     "Caipira":  {"poder": 3, "defesa": 5, "vida": 15, "muniçao": 1, "item": "Espingarda"}
# }
