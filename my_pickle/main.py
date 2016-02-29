import os

import typing # mypy
from typing import List
from typing import Any

path_file = 'forTeste.txt'

def limpa_arquivo() -> None:
    tmp_file = open(path_file, 'w')
    tmp_file.close()

def escrever_arquivo(li_numero: List[int]) -> None:
    stLista = str(li_numero)
    with open(path_file, 'r+') as f:
        f.write(stLista)


def contador_espaco(stLista: str) -> int:
    contador = 0
    for i in stLista:
        if i == ' ':
            contador +=  1
    return contador

def ponto_adicionar(stLista: str) -> List[Any]:
    aux = list() # type: List[Any]
    localVirgula = stLista.find(',')
    # caso exista virgula existe mais de um inteiro na string
    if localVirgula != -1:
        # pega o numero antes da virgula
        stNum = stLista[:localVirgula]
        # pega a string depois do espaco logo depois da virgula
        stLista = stLista[localVirgula + 1:]
        num = int(stNum)
    else:
        num = int(stLista)
    
    aux.append(num)
    aux.append(stLista)
    # aux == [numero, sub_string_sem_numero]
    return aux

def inserir_numeros(num: int) -> None:
    listaInteiro = list() # type: List[int]
    
    f_teste = open(path_file, 'r')
    for i in f_teste:
        if len(i) == 0:
            continue
        i = i[1:-1] # linha desejada
       
        fimFor = 1 + contador_espaco(i) # fornece a quantidade de elementos
        
        # "2, 3, 41, 3" transforma uma string com numeros em uma lista de int
        # [2, 3, 41, 4]
        for k in range(fimFor):
            
            chamadaFun = ponto_adicionar(i)
            numInt = chamadaFun[0]
            i = chamadaFun[1]
            # adiciona os numero que ja estavam escritos no arquivo
            listaInteiro.append(numInt)
        
        # o arquivo so tem uma linha nao eh necessario uma nova interacao
        break
    
    f_teste.close()
    listaInteiro.append(num) # adiciona o numero digitado pelo usuario
    limpa_arquivo()
    escrever_arquivo(listaInteiro)

def lista_inteiro_arquivo() -> List[int]:
    listaInteiro = list() # type: List[int]
    with open(path_file, 'r') as f_teste:
        for i in f_teste:
            if len(i) == 0:
                continue
            i = i[1: -1]
            fimFor = 1 + contador_espaco(i)
            for k in range(fimFor):
                chamadaFun = ponto_adicionar(i)
                numInt = chamadaFun[0]
                i = chamadaFun[1]
                listaInteiro.append(numInt)
    
    return listaInteiro


def dobra_elementos() -> None:
    lisInteiro = [] # type: List[int]
    listaInteiro = lista_inteiro_arquivo()
    cont = 0
    for i in lisInteiro:
        lisInteiro[cont] = i * 2
        cont = cont + 1
    escrever_arquivo(lisInteiro)

def limpa_tela() -> None:
    # windows
    if os.name == 'nt':
        os.system('cls')
    
    # posix
    else:
        os.system('clear')

if __name__ == '__main__':
    while True:
        limpa_tela()
        print('Digite done para sair.')
        print('Digite c para limpar o arquivo')
        s_num = input('Digite um numero inteiro para inserir no arqivo: ')
        try:
            num = int(s_num)
            inserir_numeros(num)
            
        except ValueError:
            if s_num == 'c':
                limpa_arquivo()
                break
            elif s_num == 'done':
                break
            else:
                print('\nEntrada invalida.')
                input('Enter to continue.')
                continue

