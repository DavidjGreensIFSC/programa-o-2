
# 1
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"O primeiro número: {num1}, é maior que o segundo número: {num2}!")
elif num2 > num1:
    print(f"O segundo número: {num2} é maior que o primeiro número: {num1}!")   
else:
    print("Os dois números são iguais!")
 
 
#2
while True:
    
    medico = int(input("Qual médico você deseja?\nDigite 1 para escolher o médico LUCAS.\nDigite 2 para escolher o médico TAYNAN.\nDigite 3 para escolher o médico VICTOR.\nQual a sua escolha?: "))

    if medico == 1:
        print("Você escolheu o médico LUCAS!")
        break
    elif medico == 2:
        print("Você escolheu o médico TAYNAN!")
        break
    elif medico == 3:
        print("Você escolheu o médico VICTOR!")
        break
    else:
        print (f"Não existe a opção: {medico}\nDigite outra opção!")


#3
frase = "python é uma excelente linguagem de programação!!!"

palavra = input("Qual palavra deseja saber se está na frase?: ").lower()

tem_na_frase = frase.find(palavra)

if  tem_na_frase == -1:
    print(f"A palavra ({palavra}) não está na frase.")

else:
    print(f"A palavra ({palavra}) está na frase.")

#4
numero = int(input("Digite qualquer número: "))
if numero % 2 == 0: 
    print('Esse número é par!') 
else:
    print('Ele é ímpar!')


#5
numero1 = int(input("Digite qualquer número: "))
numero2 = int(input("Digite qualquer número: "))
if numero1 >= 0 and numero2 >= 0:
    print("Ambos são positivos!")
elif numero1 < 0 and numero2 < 0:
    print("Ambos são negativos!")
elif numero1 < 0 or numero2 < 0: 
    print("Um dos números é negativo!")


#6
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
if number1 > number2: 
    print(f"O primeiro número: {number1}, é maior que o segundo número: {number2}")
elif number2 > number1:
    print(f"O segundo número: {number2}, é maior que o primeiro número: {number1}")
elif number1 == number2:
    print("Os valores são iguais!")
   
    
#7
print("Vamos calcular seu IMC: ")
peso = float(input("Digite seu peso (Obs: Escreva em quilos):"))
altura = float(input("Digite sua altura (Obs: Digite em metros):"))
imc = peso / (altura * altura)
print(f"O resultado do seu IMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso!")
    
elif imc > 18.5 and imc < 24.9:
    print("Peso normal!")
    
elif imc > 25 and imc < 29.9:
    print("Sobrepeso!")
    
elif imc > 30:
    print("Obesidade!")
