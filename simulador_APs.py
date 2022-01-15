## Antonio Fernandes Valadares 
## 11711ECP015

# Simulador universal de autômatos fde pilha não-deterministícos


# Função recursiva que percorre a cadeia de simbolos e retorna verdadeiro para cadeia aceita
# e falso para cadeia rejeitada

def testaCadeia(cadeia,estado,pilha):

    if(cadeia == ''):
        cadeia = '-'

    #proximo simbolo da cadeia
    simbolo = cadeia[0]
    #topo da pilha
    topo_pilha = pilha[0]

    #for para testar todas transicoes possiveis
    for transicao in conj_transicoes:
        #trata do caso onde não se adiciona nada a pilha
        if(transicao[4] == '-'):
            transicao[4] = ''
        #caso a transicao seja possivel, a transicao ocorre a subcadeia é testada 
        if (estado == transicao[0] and simbolo == transicao[1] and topo_pilha == transicao[2]):
            if(testaCadeia(cadeia[1:], transicao[3], (transicao[4] + pilha[1:]))):
                return True
        #condicao em que a transicao eh vazia, a transicao ocorre e a mesma cadeia é testada
        if (estado == transicao[0] and transicao[1] == '-' and topo_pilha == transicao[2]):
            if(testaCadeia(cadeia, transicao[3], (transicao[4] + pilha[1:]))):
                return True

    #condição de parada, quando a cadeia estiver vazia e a pilha estiver no fundo não houver mais transições
    if(cadeia == '-' and pilha == 'Z'):
        for estado_aceitacao in estados_aceitacao:
            estado_aceitacao = int(estado_aceitacao)
            if(estado_aceitacao == estado):
                return True
        return False



    return False
            

if __name__ == "__main__":

    #recebe o número de estados
    num_estados = input()

    #recebe os símbolos terminais
    simb_terminais = input()
    #cria uma lista dos simbolos
    simb_terminais = simb_terminais.split()
    #separa o número de simbolos dos simbolos
    num_simb_terminais = int(simb_terminais[0])
    del simb_terminais[0]

    #recebe os símbolos de pilha
    simb_pilha = input()
    #cria uma lista do simbolos
    simb_pilha = simb_pilha.split()
    #separa o numero de simbolos dos simbolos
    num_simb_pilha = int(simb_pilha[0])
    del simb_pilha[0]

    #recebe os estados de aceitação
    estados_aceitacao = input()
    #cria uma lista dos estados de aceitação
    estados_aceitacao = estados_aceitacao.split()
    #separa o numero de estados de aceitação
    qtde_estados_aceitacao = int(estados_aceitacao[0])
    del estados_aceitacao[0]

    #recebe o numero de transições
    num_transicoes = int(input())

    conj_transicoes = []

    #laço para receber as transições
    for i in range(0, num_transicoes):
        transicao = input()

        transicao = transicao.split()
        #converte os valores dos estados para inteiros
        transicao[0] = int(transicao[0])
        transicao[3] = int(transicao[3])

        #armazena a transicao na lista de transicoes
        conj_transicoes.append(transicao)

    #recebe o numero de cadeias
    num_entradas = int(input())

    #laço para ler e verificar as cadeias
    for i in range (0,num_entradas):
        cadeia = input()

        if(testaCadeia(cadeia,0,'Z')):
            print("aceita")
        else:
            print("rejeita")