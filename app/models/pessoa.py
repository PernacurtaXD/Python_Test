from app.models.enum.sexo import Sexo


class Pessoa:
    def __init__(self, nome: str, idade: str, sexo: Sexo):
        self.nome = self._nome_test(nome)
        self.idade = self._idade_test(idade)
        self.sexo = sexo

    def _nome_test(self, nome):
        if not nome.strip():
            raise TypeError("O nome digitado não pode ser vazio.")
        
        if nome != "Luis":
            raise TypeError("O nome digitado está incorreto.")
        
        return nome
    
    def _idade_test(self, idade):
        
        if not idade.strip():
            raise TypeError("Idade digitada incorreta.")
        

        if idade != "19":
            raise TypeError("Idade inválida")
            
        return idade  


