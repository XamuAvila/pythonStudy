import datetime
import functools

[print(x) for x in range(11) if x % 2 == 1]

# strip = trim

nome = ' ana';
print(nome.strip().capitalize())

pessoas = [' Ana', 'manuela', 'Felipe', 'PedrO']

pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas]
print(pessoas_normalizadas)

meu_set = {4, "valor", 3}
meu_dicionario = {'nome': 'Samuel'}

print(meu_dicionario['nome'])


##Classes

class Player:
    def __init__(self, nome):
        self.nome = nome
        self.numeros = (13, 4, 52, 23, 67, 82)

    def total(self):
        return sum(self.numeros)


jogador_1 = Player('Samuel')
jogador_2 = Player('Yasmin')

print(jogador_1.total())


class Funcionario:
    aumento = 1.04

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}

    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

    @classmethod
    def definir_novo_aumento(cls):
        cls.aumento = 1.20

    @staticmethod
    def util_day(day):
        print(day.weekday())
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


fabio = Funcionario('Fabio', 7000)
Funcionario.definir_novo_aumento()
fabio.aplicar_aumento()
print(fabio.dados())


class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()


admin = Admin('Admin Samuel', 9000)
print(admin.dados())
print(admin.atualizar_dados('Novo Nome'))

print(Funcionario.util_day(datetime.date(2022, 7, 29)))

# args ==> argumentos
# kwargs ==> argumentos de palavaras chave

#rest parameter
def meu_metodo(*args):
    return sum(args)

print(meu_metodo(5,7,6,7))


#decorators

def my_decorator(function):
    @functools.wraps(function)
    def func_que_roda_funcao():
        print("Embrulhando funcao no decorator")
        function()
        print("Fechando embrulho")
    return func_que_roda_funcao()

@my_decorator
def my_function():
    print("I'm a function")