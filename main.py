class Integrante_IFRN:
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
class professor(Integrante_IFRN):
    def __init__(self, mensagem, mensa_prof):
        super().__init__(mensagem)
        self.mensa_prof = mensa_prof

class aluno(Integrante_IFRN):
    def __init__(self, mensagem, mensa_aluno):
        super().__init__(mensagem)
        self.mensa_aluno = mensa_aluno



integrante = Integrante_IFRN("Seja bem-vindo(a) ao IFRN!!!")
print(integrante.mensagem)

prof = professor("Meus alunos são os melhores!!!", "Mensagem específica do professor.")
print(prof.mensagem)       
print(prof.mensa_prof) 

al = aluno("Vou estudar pra tirar 100 em POO!!!", "Mensagem específica do aluno.")
print(al.mensa_aluno)  