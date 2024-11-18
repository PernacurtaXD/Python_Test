import pytest
from app.models.pessoa import Pessoa 
from ..models.enum.sexo import Sexo




def test_nome_invalido():
    with pytest.raises(TypeError, match= "O nome digitado está incorreto."):
        Pessoa("", "19", Sexo.MASCULINO.value)
