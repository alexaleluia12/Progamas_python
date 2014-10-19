
path_file = 'forTeste.txt';
##  esta pronto ##
def limpaArquivo():
    f_teste = open(path_file, 'w')
    f_teste.close()

def escreverArquivo(li_numero): # nao tem retoro, recebe uma lista como parametro o com todos os valores ja adicionados. apenas escreve no arquivo
    stLista = str(li_numero)
    f_teste = open(path_file, 'r+')
    f_teste.write(stLista)
    f_teste.close()
    
def contadorEspaco(stLista): #recebe uma string como paramentro e retorna a quantidade de espacos que existe na string
    contador = 0
    for i in stLista:
        if i == ' ':
            contador = contador + 1
    return contador

def prontoAdicionar(stLista): # recebe uma string e retorna um inteiro
    aux = list()
    localVirgula = stLista.find(',')
    if localVirgula != -1: # caso exista virgula existe mais de um inteiro na string
        
        stNum = stLista[:localVirgula] # pega o numero antes da virgula
        stLista = stLista[localVirgula + 1:] # pega a string depois do espaco logo depois da virgula
        num = int(stNum)
    else: # caso nao so sobra o ultimo elemento que pode ser transformado diteto em inteiro
        
        num = int(stLista)
    
            
    
    # num = int(stNum)
    
    
    aux.append(num) # depois de um dos dois casos e adiconado ao vetero
    aux.append(stLista)
    return aux # retor na uma lista. 1 e um numero . 2 e uma string ja tirado o numero que esta enviando. Assim e mais facil de encontrar os outros elementos

        
    

def inserirNumeros(num):
    listaInteiro = list()
    
    f_teste = open(path_file, 'r')
    for i in f_teste:
        if len(i) == 0:
            continue
        i = i[1:-1]   # e uma string
       
        fimFor = 1 + contadorEspaco(i) # fornece a quantidade de elementos
        for k in range(fimFor):

            chamadaFun = prontoAdicionar(i)
            numInt = chamadaFun[0]
            i = chamadaFun[1]
            listaInteiro.append(numInt) # adiciona os numero que ja estavam escritos no arquivo
            
            
    f_teste.close()
    listaInteiro.append(num) # adiciona o numero digitado pelo usuario
    limpaArquivo()
    escreverArquivo(listaInteiro)

def listaInteiroArquivo(): # retorna uma lista de inteiros
    listaInteiro = list()
    f_teste = open(path_file, 'r')
    for i in f_teste:
        if len(i) == 0:
            continue
        i = i[1: -1]
        fimFor = 1 + contadorEspaco(i)
        for k in range(fimFor):
            chamadaFun = prontoAdicionar(i)
            numInt = chamadaFun[0]
            i = chamadaFun[1]
            listaInteiro.append(numInt)

    return listaInteiro   
        
    
    
            
            
        

def dobraElementos():
## o que deve fazer ##
# pegar a lista de inteiros do arquivo
# multiplicar por dois cada elemento
# escrever o resultado no arquivo novamente
    lisInteiro = listaInteiroArquivo()
    cont = 0
    for i in lisInteiro:
        lisInteiro[cont] = i * 2
        cont = cont + 1
    escreverArquivo(lisInteiro)
    


    
        
                
            
    
     



while True:
    print 'Digite done para sair.'
    print 'Digite c para linpar o arquivo'
    s_num = raw_input('Digite um numero inteiro para inserir no arqivo: ')
    try:
        num = int(s_num)
        
        inserirNumeros(num)
    except:
        if s_num == 'c':
            limpaArquivo()
            break
        elif s_num == 'done':
            break
        else:
            print '\nEntrada invalida.'
            continue

       
#dobraElementos()


