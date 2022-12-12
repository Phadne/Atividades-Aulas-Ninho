class Pessoa:
    def __init__(self,nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo

    def desativar(self):
        self.ativo = False
        print("Carla foi desativada com sucesso")

if __name__ == "__main__":
    pessoal = Pessoa("Carla", "F", "888670", True)
    pessoal.desativar()
