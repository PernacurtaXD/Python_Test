from app.models.enum.sexo import Sexo


class Pessoa:
    def __init__(self, nome: str, idade: str, sexo: Sexo):
        self.nome = self._nome_test(nome)
        self.idade = idade
        self.sexo = sexo

    def _nome_test(self, nome):
        if not nome.strip():
            raise TypeError("O nome digitado está incorreto.")
        return nome
