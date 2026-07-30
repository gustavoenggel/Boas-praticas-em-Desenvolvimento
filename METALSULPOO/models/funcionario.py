class Funcionario:
    def __init__(self,id,nome,cargo,salario,setor):
        self.__id = id
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__setor = setor

    def apresentar(self):
        print(f"Id do funcionario: ",self.__id)
        print(f"Nome do Funcionario: ",self.__nome)
        print(f"Cargo: ",self.__cargo)
        print(f"Salario: ",self.__salario)
        print(f"Setor: ",self.setor.nome)

    def trocar_cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    @property
    def setor(self):
        return self.__setor

    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome
    @property
    def cargo(self):
        return self.__cargo
    @property
    def salario(self):
        return self.__salario


    #Setters
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @cargo.setter
    def cargo(self, cargo):
        if cargo == "":
            raise ValueError("O cargo nao pode estar vazio")
        self.__cargo = cargo
        

    @salario.setter
    def salario(self, salario, valor):
        if valor <0:
            self.__salario = salario
        else:
            raise ValueError("numero deve ser positivo")

    def aumentar_salario(self,valor):
        if valor <=0:
            raise ValueError(f"O aumento {valor} deve ser maior que 0")
        self.__salario += valor
