class Entidade:
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, vida_atual: int, esquiva: int):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_atual
        self.esquiva = esquiva

    def estar_vivo(self):
        if self.vida_atual > 0:
            return True
        return False

    # Receber dano não pode ser valor negativo
    def receber_dano(self, dano):
        self.vida_atual -= dano
        if self.vida_atual <= 0:
            self.vida_atual = 0


            

    # Curar não pode ultrapassar a vida máxima
    def curar(self,  cura):
        self.vida_atual += cura
        if self.vida_atual >= self.vida_maxima:
            self.vida_atual = self.vida_maxima
            print("Cura maxima")
        else:
            print("Voce foi curado")


# boneco = Entidade("Arthur Morgan", 100, 100, 200, 150, 10)

# # boneco.estar_vivo()
# # boneco.receber_dano(100)
# boneco.curar(10)
