class Tamagotchi:
    def __init__(self, nome,idade,peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.dormindo = False
        self.falando = False
        self.acordou = False
        self.calou = False
        self.paroudecomer = False


    def comer(self,comida):
        if self.comendo == True:
            print(f"{self.nome} já está comendo...")

    def parardecomer (self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer...")
            self.comendo = False
        else:
            print(f"{self.nome} não estava comendo...")

    def dormir (self):
        if self.dormindo == True:
            print(f"{self.nome} já está dormindo...")
        else:
            print(f"{self.nome} foi dormir...")
            self.dormindo = True

    def acordar(self):
        if self.dormindo == True:
            print(f"{self.nome} acordou...")
            self.dormindo = False
        else:
            print(f"{self.nome} já estava acordado....")

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} já está falando...")
        else:
            print(f"{self.nome} começou a falar...")
            self.falando = True

    def paroudefalar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar...")
        else:
            print(f"{self.nome} não estava falando...")

    def status(self):
        print(f"Fome de {self.nome}: {self.fome}")
