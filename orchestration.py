import requests
import datetime
from collections import Counter


def verificando_arquivo_retornando_validos():
    try:
        conteudo_valido = []
        file = open(r"data_file.txt", "r+")
        conteudo = file.readlines()
        for linha in conteudo:
            valores_linha = linha.split(';')
            valor_valido = verificador_dados(valores_linha)
            if valor_valido:
                conteudo_valido.append(valor_valido)
        print(conteudo_valido)
        conteudo_valido_sem_duplicidade_mensagem = verificando_duplicidade_mensagem(conteudo_valido)
        print(conteudo_valido_sem_duplicidade_mensagem)
        return conteudo_valido_sem_duplicidade_mensagem
    except Exception as e:
        raise e


def verificando_duplicidade_mensagem(lista_mensagens_aptas):
    lista_aptas_sem_duplicidade = []
    lista_duplicados = []
    registros_duplicados = Counter(lista['telefone'] for lista in lista_mensagens_aptas)
    for key, value in registros_duplicados.items():
        if value > 1:
            for registro in lista_mensagens_aptas:
                if registro["telefone"] == key:
                    lista_duplicados.append(registro)
                else:
                    id_mensagem = registro["id_mensagem"]
                    id_broker = registro["id_broker"]
                    formato_response = f"{id_mensagem};{id_broker}"
                    lista_aptas_sem_duplicidade.append(formato_response)
    primeiro_registro_lista_duplicados = lista_duplicados[0]
    for linha in lista_duplicados[1:]:
        if primeiro_registro_lista_duplicados["hora_registro"] < linha["hora_registro"]:
            id_mensagem = primeiro_registro_lista_duplicados["id_mensagem"]
            id_broker = primeiro_registro_lista_duplicados["id_broker"]
            formato_response = f"{id_mensagem};{id_broker}"
            lista_aptas_sem_duplicidade.append(formato_response)
    return lista_aptas_sem_duplicidade


def verificador_dados(valores_linha):
    hora_registro = valores_linha[4]
    mensagem = valores_linha[5]
    tempo_verificado = verificador_tempo(hora_registro)
    mensagem_verificada = verificador_tamanho_mensagem(mensagem)
    if tempo_verificado == "ok" and mensagem_verificada == "ok":
        if valores_linha[1] != "11":
            ddd = valores_linha[1]
            numero = valores_linha[2]
            numero_verificado = validando_numero_oferecido(ddd, numero)
            if numero_verificado == "ok":
                telefone = f"{ddd}{numero}"
                consultar_numero_black_list = verificador_black_list(telefone)
                if consultar_numero_black_list == "ok":
                    nome_op = valores_linha[3]
                    id_broker = verificar_retornar_id_broker(nome_op)
                    formato_response = {
                        "id_mensagem": valores_linha[0],
                        "id_broker": id_broker,
                        "telefone": telefone,
                        "hora_registro": hora_registro
                    }
                    return formato_response


def validando_numero_oferecido(ddd, numero):
    if len(ddd) == 2:
        lista_numero_telefone = list(numero)
        if int(lista_numero_telefone[1]) > 6 and len(numero) == 9 and int(lista_numero_telefone[0]) == 9:
            return "ok"


def verificador_tamanho_mensagem(mensagem):
    tamanho_mensagem = len(mensagem)
    if tamanho_mensagem < 141:
        return "ok"


def verificador_tempo(hora_registro):
    hora_maxima_permitida = "19:59:59"
    horario_permitido_envio = datetime.datetime.strptime(hora_maxima_permitida, '%H:%M:%S')
    hora_registro_timestamp = datetime.datetime.strptime(hora_registro, '%H:%M:%S')
    if hora_registro_timestamp < horario_permitido_envio:
        return "ok"


def verificar_retornar_id_broker(nome_op):
    id_broker = {
        "1": ["VIVO", "TIM"],
        "2": ["CLARO", "OI"],
        "3": ["NEXTEL"]
    }
    for linha in id_broker.items():
        for operadoras in linha[1]:
            if nome_op == operadoras:
                return linha[0]


def verificador_black_list(telefone):
    url = f"https://front-test-pg.herokuapp.com/blacklist/{telefone}"
    response = requests.get(url)
    if response.status_code == 404:
        return "ok"
    else:
        return "nok"


if __name__ == '__main__':
    verificando_arquivo_retornando_validos()
