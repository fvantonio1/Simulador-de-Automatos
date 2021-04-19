## Antonio Fernandes Valadares  
## 11711ECP015

import sys


#funcao recursiva para percorrer a cadeia de simbolos
def testaCadeia(cadeia,estado):

    global conj_est_aceitacao, conj_transicoes

    #condiçao de parada da recursao
    #quando a cadeia estiver vazia verifica se o estado atual é de aceitacao
    if((cadeia == '') or (cadeia == '-')):  
        for estado_aceitacao in conj_est_aceitacao:
            estado_aceitacao = int(estado_aceitacao) #converte o estado de aceitacao para um int
            if(estado_aceitacao == estado):
                return True
        return False

    simbolo = cadeia[0]
    #laço para verificar as possiveis transicoes
    for transicao in conj_transicoes:
        if((transicao[0] == estado) and (transicao[1] == simbolo)):
            if(testaCadeia(cadeia[1:],transicao[2])):
                return True
            
    
    
    return False



if __name__ == "__main__":

    #recebe o numero de estados 
    num_estados = input()


    #recebe o conjunto de simbolos terminais
    conj_simb_terminais = input()

    conj_simb_terminais = conj_simb_terminais.split() #Cria uma lista dos simbolos terminais
    num_simb_terminais = int(conj_simb_terminais[0]) #Separa o numero de simbolos terminais dos simbolos terminais
    del conj_simb_terminais[0]


    #recebe o conjunto de estados de aceitacao
    conj_est_aceitacao = input()

    conj_est_aceitacao = conj_est_aceitacao.split() #Cria uma lista dos estados terminais
    qtd_est_aceitacao = int(conj_est_aceitacao[0]) #Separa o numero de estados terminais
    del conj_est_aceitacao[0]


    #recebe o numero de transicoes
    num_transicoes = int(input()) 

    conj_transicoes = [] #Cria uma lista para as transicoes

    #laço para tratar das entradas das transicoes
    for i in range(0,num_transicoes):
        #recebe transicao
        transicao = input()
        #Cria uma lista para cada transição onde o primeiro valor eh o estado de origem o segundo o simbolo terminal e o terceiro o estado de destino
        transicao = transicao.split()
        #Converte os valores dos estados para valores inteiros
        transicao[0] = int(transicao[0])
        transicao[2] = int(transicao[2])

        #Armazena a transicao na lista de conjuntos de transicoes
        conj_transicoes.append(transicao)


    #recebe o numero de cadeias de entrada
    num_entradas = int(input())

    #laço para ler e verificar as cadeias de entrada
    for i in range(0,num_entradas):
        #recebe uma cadeia
        cadeia = input()

        #verifica se ela é aceita ou rejeitada
        if(testaCadeia(cadeia,0)):
            print("aceita")
        else:
            print("rejeita")



