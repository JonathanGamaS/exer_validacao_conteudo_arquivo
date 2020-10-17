import pytest
from orchestration import verificando_arquivo_retornando_validos


def test_verificando_comportamento_linha_formato_diferente():
    arquivo = open(r"data_file_test.txt", "r+")
    resposta = verificando_arquivo_retornando_validos(arquivo)
    assert isinstance(resposta, list)

