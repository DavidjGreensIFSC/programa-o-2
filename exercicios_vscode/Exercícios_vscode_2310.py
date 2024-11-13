#1
numero_inserido_pelo_usuario = int(input("Digite o primeiro número: "))
segundo_numero_inserido_pelo_usuario = int(input("Digite outro número: "))
soma_dos_numeros = numero_inserido_pelo_usuario + segundo_numero_inserido_pelo_usuario
print(f"A soma de {numero_inserido_pelo_usuario} + {segundo_numero_inserido_pelo_usuario} resulta em {soma_dos_numeros}")

#2
digito_digitado_pelo_usuario = int(input("Digite um número: "))
if digito_digitado_pelo_usuario > 0:
    print(f"o número {digito_digitado_pelo_usuario} é positivo!")
elif digito_digitado_pelo_usuario == 0:
    print("Você digitou o número 0!")
else:
    print(f"o número {digito_digitado_pelo_usuario} é negativo!")

#3
numero_digitado_pelo_usuario = int(input("Digite um número: "))
outro_número_digitado_pelo_usuario = int(input("Digite mais um número: "))
if numero_digitado_pelo_usuario > outro_número_digitado_pelo_usuario:
    print(f"O número {numero_digitado_pelo_usuario} é maior que {outro_número_digitado_pelo_usuario}")
elif numero_digitado_pelo_usuario == outro_número_digitado_pelo_usuario:
    print(f"Você digitou {outro_número_digitado_pelo_usuario} duas vezes!")
else:
    print(f"O número {numero_digitado_pelo_usuario} é menor que {outro_número_digitado_pelo_usuario}")