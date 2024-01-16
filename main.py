import json
import random
import requests

PALAVRAS_UTF8 = 'https://www.ime.usp.br/~pf/dicios/br-utf8.txt'
PALAVRAS_SEM_ACENTO = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

HOME_ROW = 'aoeuhtns'
FULL_HOME_ROW = HOME_ROW + 'id'
HOME_ROW_RIGHT = FULL_HOME_ROW + 'pfcrlkmv'
HOME_ROW_LEFT = FULL_HOME_ROW + 'ygçqjxbwz'
FULL = FULL_HOME_ROW + HOME_ROW_RIGHT + HOME_ROW_LEFT

if __name__ == '__main__':

    print('Bem vindo ao jogo de digitação.')

    print('Escolha o modo de jogo: ')
    print('1 - Home Row')
    print('2 - Full Home Row')
    print('3 - Home Row Right')
    print('4 - Home Row Left')
    print('5 - Full')
    modo = input('>> ')

    if modo == '1':
        teclado = HOME_ROW
    elif modo == '2':
        teclado = FULL_HOME_ROW
    elif modo == '3':
        teclado = HOME_ROW_RIGHT
    elif modo == '4':
        teclado = HOME_ROW_LEFT
    elif modo == '5':
        teclado = FULL
    else:
        print('Modo de jogo inválido.')
        exit()

    print('Escolha uma opção: ')
    print('1 - Palavras com acentos')
    print('2 - Palavras sem acentos')
    opcao = input('>> ')

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

    palavras = r.text.splitlines()

    selecionadas = []
    limite = 1000

    random.shuffle(palavras)
    # print(palavras)
    # pega uma palavra aleatória da lista
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
