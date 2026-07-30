class Setor:
    def __init__(self,id, nome):
        self.__id = id
        self.__nome = nome

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def apresentar(self):
        print("=== Setor ===")
        print(f"Id: {self.id}")
        print(f"Nome do colaborador: {self.nome}")

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == "":
            raise ValueError ("O nome do setor nao pode estar vazio")
        self.__nome = novo_nome
