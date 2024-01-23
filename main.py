import json
import random
import requests

# ------------------------------------------------------------------------------
#                     variáveis globais para todo o programa                   #
# ------------------------------------------------------------------------------

# links para as palavras
PALAVRAS_UTF8 = 'https://www.ime.usp.br/~pf/dicios/br-utf8.txt'
PALAVRAS_SEM_ACENTO = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

# linhas do teclado
HOME_ROW = 'aoeuhtns'
FULL_HOME_ROW = HOME_ROW + 'id'
HOME_ROW_RIGHT = FULL_HOME_ROW + 'pfcrlkmv'
HOME_ROW_LEFT = FULL_HOME_ROW + 'ygçqjxbwz'
FULL = FULL_HOME_ROW + HOME_ROW_RIGHT + HOME_ROW_LEFT

# quantidade de palavras geradas
LIMITE = 1000

# ------------------------------------------------------------------------------
#                                    Funções                                   #
# ------------------------------------------------------------------------------

def saudacao():
    print('Bem-vindo!')

def escolhe_layout():
    print('Escolha as teclas que serão usadas: ')
    print('1 - Home Row (aoeuhtns)')
    print('2 - Full Home Row (aoeuhtnsid)')
    print('3 - Home Row Right (aoeuhtnsidpfcrlkmv)')
    print('4 - Home Row Left (aoeuhtnsidygçqjxbwz)')
    print('5 - Full')
    modo = input(' >> ')

    if modo == '1':
        return HOME_ROW
    elif modo == '2':
        return FULL_HOME_ROW
    elif modo == '3':
        return HOME_ROW_RIGHT
    elif modo == '4':
        return HOME_ROW_LEFT
    elif modo == '5':
        return FULL
    else:
        print('Modo de jogo inválido.')
        exit()

def escolhe_dicionario():
    print('Escolha uma opção: ')
    print('1 - Palavras com acentos')
    print('2 - Palavras sem acentos')
    opcao = input(' >> ')

    if opcao == '1':
        r = requests.get(PALAVRAS_UTF8)
    elif opcao == '2':
        r = requests.get(PALAVRAS_SEM_ACENTO)
    else:
        print('Opção inválida.')
        exit()

    if r.status_code != 200:
        print('Erro ao obter palavras do site.')
        exit()

    return r.text.splitlines()

def define_quantidade():
    print('Digite a quantidade de palavras que deseja gerar: ')
    quantidade = input(' >> ')

    if quantidade.isdigit():
        return int(quantidade)
    print('Quantidade inválida.')
    exit()


def seleciona_palavras(teclado, palavras, limite):
    selecionadas = []
    count = 0

    random.shuffle(palavras)
    for palavra in palavras:
        for letra in palavra:
            if letra.lower() not in teclado:
                break
        else:
            if palavra not in selecionadas:
                selecionadas.append(palavra.lower())
                limite -= 1
                if limite == 0:
                    break

    with open('resultado.txt', 'w') as arq:
        arq.write(' '.join(selecionadas))


# ------------------------------------------------------------------------------
#                                   Main                                       #
# ------------------------------------------------------------------------------
if __name__ == '__main__':

    saudacao()
    teclado = escolhe_layout()
    palavras = escolhe_dicionario()
    limite = define_quantidade()
    seleciona_palavras(teclado, palavras, limite)
