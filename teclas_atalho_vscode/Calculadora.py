class Calculadora():
def __init__ (self, num1, num2):
self.num1 = num1
self.num2 = num2

def soma(self):
    return self.num1 + self.num2
def subtracao(self):
    return self.num1 - self.num2
def multiplicacao(self):
    return self.num1 * self.num2
def divisao(self):
    return self.num1 / self.num2
def exponenciacao(self):
    return self.num1 ** self.num2
def divisao_inteira(self):
    return self.num1 // self.num2
def modulo(self):
    return self.num1 % self.num2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = Calculadora(num1, num2)

print("Escolha 1 para SOMA")
print("Escolha 2 para SUBTRAÇÃO")
print("Escolha 3 para DIVISÃO")
print("Escolha 4 para EXPONENCIAÇÃO")
print("Escolha 5 para DIVISÃO INTEIRA")
print("Escolha 7 para MÓDULO")]
escolha = int(input('Digite o número da operação: '))
if escolha == 1:
    print(f"O resultado da soma entre {num1} e {num2} é: ", operacao.soma())
elif escolha == 2:
    print(f"O resultado da subtração entre {num1} e {num2} é: ", operacao.subtracao())
elif escolha == 3:
    print(f"O resultado da divisão entre {num1} e {num2} é: ", operacao.divisao())
elif escolha == 4:
    print(f"O resultado da exponencição entre {num1} e {num2} é: ", operacao.exponenciacao())
elif escolha == 5:
    print(f"O resultado da divisão inteira entre {num1} e {num2} é: ", operacao.divisao_inteira())
elif escolha == 5:
    print(f"O resultado da módulo entre {num1} e {num2} é: ", operacao.modulo())