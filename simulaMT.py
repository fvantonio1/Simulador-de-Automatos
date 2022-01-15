## Antonio Fernandes Valadares  
## 11711ECP015



def testaCadeia(estado_atual, pos_fita, fita, k):
    k += 1
    print(k)
    #condição de parada da recursão quando o estado atual é um estado de aceitação
    if(estado_atual == estado_aceitacao):
        return True


    #Procura transições adequadas
    for transicao in conj_transicoes:
        if(estado_atual == transicao[0] and fita[pos_fita] == transicao[1]):
            #atualiza a posição na fita
            fita[pos_fita] = transicao[3]

            #move a ponteiro na fita para direita ou esquerda
            if(transicao[4]=='D'):
                pos_fita += 1
            if(transicao[4]=='E'):
                pos_fita += -1

            #testa a cadeia a partir do novo estado e da fita atualizada
            return testaCadeia(transicao[2], pos_fita, fita, k)


    return False


if __name__ == "__main__":

    #recebe o numero de estados
    n_estados = int(input())


    #recebe o numero e o conjunto de simbolos terminais
    simb_terminais = input()
    simb_terminais = simb_terminais.split()

    num_simb_terminais = simb_terminais[0]
    del simb_terminais[0]


    #recebe o conjunto de simbolos de fita
    simb_fita = input()
    simb_fita = simb_fita.split()

    num_simb_fita = simb_fita[0]
    del simb_fita[0]


    #recebe o estado de aceitação
    estado_aceitacao = int(input())
    #if(estado_aceitacao > n_estados-1):
    #    print("Estado de aceitação inválido")
        #exit(0)


    #recebe o número de transições
    num_transicoes = int(input())

    
    #recebe as transicoes
    conj_transicoes = []
    for i in range(0, num_transicoes):
        transicao = input()

        transicao = transicao.split()
        transicao[0] =  int(transicao[0])
        transicao[2] =  int(transicao[2])

        conj_transicoes.append(transicao)

    
    #recebe o número de cadeias a seque srem avaliadas
    num_cadeias = int(input())


    #laço para receber e verificar as cadeias
    for i in range(0, num_cadeias):
        cadeia = input()

        #Cria a fita da MT
        fita = list(cadeia+'B')


        if(testaCadeia(0, 0, fita, 0)):
            print("aceita")
        else:
            print("rejeita")
