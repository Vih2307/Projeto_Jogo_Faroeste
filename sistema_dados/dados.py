import random


class SistemaDados:

    def rolar_d6(self):
        return random.randint(1, 6)

    def rolar_d20(self):
        return random.randint(1, 20)
