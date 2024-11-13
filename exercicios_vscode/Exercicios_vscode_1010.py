#1
"""1)  Crie e inicialize uma variável do tipo inteiro. Enquanto o valor dessa variável for 
menor ou igual a um valor definido por você, exiba uma mensagem na tela e o 
valor dessa variável. Explique em um comentário como o controle do laço vai 
funcionar. """

import time
# "import time" Apenas para deixar um intervalo entre os valores
limite = 10
valor = 0
while valor <= limite:
    print(f"Valor da variável: {valor}")
    time.sleep(1)
    # "time.sleep()" Da um certo tempo antes de executar outra linha de código
    valor += 1
    
"""O "while" foi configurado para repetir o código enquanto o "valor"
for menor que o  "limite", quando o "valor" for igual ao "limite" o
código se encerra, pois, se passar do limite, a condição do "while"
não é mais verdadeira."""


#2
"""2)  Escreva um programa que gera um número aleatório entre 0 a 10, salvando 
esse número em uma variável. Solicite ao usuário que tente adivinhar o 
número que foi gerado aleatoriamente através da digitação via stdin. Caso o 
usuário acerte o número, exiba uma mensagem parabenizando-o e mostrando 
na mensagem o número adivinhado. Utilize a instrução  “import”  para que a 
biblioteca Random possa ser utilizada. O número aleatório deverá ser 
gerado através da função randint. Restrinja ao máximo de 5 tentativas por 
parte do usuário, caso não acerte, exiba mensagem e termine o programa. """

import random

numero_aleatorio = random.randint(0, 10)
print("Um número aleatório de 0 a 10 foi gerado!")

chute = 0
chances = 5

while chute != numero_aleatorio:
    chute = input("Tente adivinhar o número gerado: ")
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
    else: 
        print("Digite um número válido!!!")
    if chute != numero_aleatorio:
        print("Número incorreto!")
        
    if chute == numero_aleatorio:
        print(f"Parabéns você acertou era o número {numero_aleatorio}!!!")
        break
    if chances == 0:
        print(f"Que pena suas chances acabaram! O número correto era: {numero_aleatorio}")
        break
print("### FIM DE JOGO ###")           
 
    
#3
"""3)  Escreva um programa que verifica se um endereço URL de um site foi digitado 
levando-se em conta o prefixo “www.” e o sufixo “.com.br”. Se o endereço foi 
digitado nesse formato corretamente, exiba mensagem, inclusive mostrando o 
endereço digitado, e finalize o programa. Se não digitou corretamente, exiba 
uma mensagem informando que a URL é inválida, mostre o endereço no 
formato errado e solicite ao usuário que digite novamente a URL do site. Uma 
forma de resolver esse problema é utilizar métodos da classe String do Python, 
como por exemplo: startswith() e endswith(). A documentação desses métodos 
pode ser encontrada em: https://docs.python.org/pt-
br/3/library/stdtypes.html.dgs 
Enquanto a URL informada não estiver correta, o programa não deve ser 
finalizado."""

while True:
    url = input("Digite seu URL corretamente: ")
    resultado = url.startswith('www.')
    resultado = url.endswith('.com.br')
    if resultado == False:
        print(f"O endereço: {url} é inválido!")
        print("Tente novamente!")
    else:
        print(f"O endereço: {url} é válido!")
        break
    