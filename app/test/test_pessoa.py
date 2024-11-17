import pytest
from models.pessoa import Pessoa
from models.enum.sexo import Sexo


@pytest.fixture
def criar_pessoa(Pessoa):
    return Pessoa("Luis", "18", Sexo.MASCULINO)

