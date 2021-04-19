# Simulador-de-Automatos

Algoritmos que simula um autômato finito determinístico ou não, e retorna para cada cadeia se ela é aceita ou rejeitada.

Exemplo de entrada:

![image](https://user-images.githubusercontent.com/35939169/115295252-ec01ae00-a12f-11eb-9233-8282734c3e51.png)

3 #Número de estados

2 a b #Quantidade e os simbolos terminais

1 2 #Quantidade e os estados finais

6 #Número de transições

#Transições
0 a 1

0 b 1

1 a 1

1 b 2

2 a 0

2 b 2

10 #Número de cadeis a serem testadas

#Cadeais a serem testadas
abbbba

aabbbb

bbabbabbabbb

bbbbbbbbbbb

-

abababababab

bbbbaabbbb

abba

a

aaa


Saída:

rejeita

aceita

aceita

aceita

rejeita

rejeita

aceita

rejeita

rejeita

rejeita


