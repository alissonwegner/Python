from datetime import datetime
from random import randint
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f'nome:{self.nome} e idade de: {self.idade}')

    @staticmethod
    def gerar_id():
        rand = randint(1000, 9999)
        return rand