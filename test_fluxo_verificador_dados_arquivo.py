import unittest


class TestSum(unittest.TestCase):

    def test_fluxo_funcao_principal_orchestration(self):
        from code.orchestration import verificando_arquivo_retornando_validos
        arquivo = open(r"data_file.txt", "r+")
        response = verificando_arquivo_retornando_validos(arquivo)
        self.assertIsInstance(response, list)

    def test_arquivo_vier_layout_diferente(self):
        from code.orchestration import verificando_arquivo_retornando_validos
        from code.orchestration import LayoutException
        arquivo = open(r"data_file_test.txt", "r+")
        with self.assertRaises(LayoutException):
            response = verificando_arquivo_retornando_validos(arquivo)


if __name__ == '__main__':
    unittest.main()
