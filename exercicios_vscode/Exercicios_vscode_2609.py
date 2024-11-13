#1
print("Digite dois números")

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"A soma: : {soma} - A subtração: {subtracao} - A multiplicação: {multiplicacao} A divisão: {divisao}")

#2
print("Vamos calcular seu IMC: ")
peso = float(input("Digite seu peso (Obs: Escreva em quilos):"))
altura = float(input("Digite sua altura (Obs: Digite em metros):"))
imc = peso / (altura * altura)
print(f"O resultado do seu IMC: {imc:.2f}")
if imc > 40:
    print("Você está muito obeso!")
    
elif imc < 18.5:
    print("Você está muito magro!")
    
elif imc > 18.5 and imc < 24.9:
    print("Você está no peso normal!")
    
elif imc > 25 and imc < 29.9:
    print("Você está com excesso de peso!")
    
elif imc > 30 and imc < 34.9:
    print("Você está com obesidade classe I!")
    
elif imc > 35 and imc < 39.9 :
    print("Você está com obesidade classe II!")
    
elif imc > 40:
    print("Você está com obesidade classe III!")  

#3
frase = "Bem vindo turma da Programação II ao mundo da programação Python!!!" [:: - 1 ]
print(frase)

#4 
import random
tamanho_da_senha_a_ser_gerada = int(input("Digite o tamanho da senha (Max: 128): "))
uuid_gerador_senha = '35b35f68-9687-4ca6-bb79-f59201d40b0739e5b006-f4ab-49cb-a072-6549876b35dc'
senha_gerada = "  ".join(random.sample(uuid_gerador_senha, tamanho_da_senha_a_ser_gerada))
print(f"Senha gerada com {tamanho_da_senha_a_ser_gerada} caracteres: {senha_gerada}")

#5
import datetime
agora = datetime.datetime.now()
print(agora).strftime("%d/%m/%Y  %H:%M:%S")