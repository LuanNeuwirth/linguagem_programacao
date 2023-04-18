class Aluno:
    def int(self, matricula, nome, nota1, nota2, nota_trabalho):
        self.matricula = matricula
        self.nome = nome 
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota_trabalho = nota_trabalho

def media(self):
    return (self.nota1 *2.5) + (self.nota2 * 2.5) + (self.nota_trabalho *2)
def final(self):
    media = self.media()
    if media < 4.0:
        return 0.0
    elif media <= 7.0:
        return "aprovado"
    else:
        return final: (10.0 - media:.2f)

    
