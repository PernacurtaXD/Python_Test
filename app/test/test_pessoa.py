import pytest
from app.models.pessoa import Pessoa 
from ..models.enum.sexo import Sexo


def test_nome_vazio():
    with pytest.raises(TypeError, match= "O nome digitado não pode ser vazio."):
        Pessoa("", "19", Sexo.MASCULINO.value)

def test_idade_vazio():
    with pytest.raises(TypeError, match= "Idade digitada incorreta."):
        Pessoa("Luis", "", Sexo.MASCULINO.value)

def test_nome_invalido():
    with pytest.raises(TypeError, match= "O nome digitado está incorreto."):
        Pessoa("Marcos", "19", Sexo.MASCULINO.value)

def test_idade_invalida():
    with pytest.raises(TypeError, match= "Idade inválida"):
        Pessoa("Luis", "15", Sexo.MASCULINO.value)