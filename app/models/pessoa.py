from models.enum.sexo import Sexo


class Pessoa:
    def __init__(self, nome: str, idade: str, sexo: Sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Idade: {self.idade} - Sexo:{self.sexo.value}"