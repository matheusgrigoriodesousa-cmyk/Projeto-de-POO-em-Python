# criando a classe Nota
class Nota:
    def __init__(self, np1, np2, pim): 
        self.np1 = np1 
        self.np2 = np2
        self.pim = pim

# Verificando a media e a situação do aluno
    def calcular_media(self): 
        media = (self.np1 * 4 + self.np2 * 4 + self.pim * 2) / 10
        print("Média:", media)

        if media >= 6: 
            print("Aluno Aprovado")
        elif media >= 4: 
            print ("Aluno em Recuperação")
        else: 
            print("Aluno Reprovado")


# criando objeto
aluno = Nota(7, 5, 6) 

# chamando método
aluno.calcular_media() 