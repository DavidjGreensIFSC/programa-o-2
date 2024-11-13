class calculadora():
        def _init_(self,num1,num2):
                self.num1 = num1 
                self.num2 = num2 
        def soma(self):
                return self.num1 + self.num2 
        def subtraçãoo(self):
                return self.num1 - self.num2
        def multiplicação(self):
                return self.num1 * self.num2
        def divisão(self):
                return self.num1 / self.num2
        def exponenciação(self):
                return self.num1 ** self.num2
        def divisão_interia(self):
                return self.num1 // self.num2
        def modulo(self):
                return self.num1 % self.num2
        
num1 = int(input("Digite o seu primeiro número:  "))
num2 = int(input("Digite o segundo número:  "))
operação = calculadora(num1, num2)

print('escolha 1 para SOMA')
print('escolha 2 para SUBTRAÇÃO')
print('escolha 3 para MULTIPLICAÇÃO')
print('escolha 4 para DIVISÃO')
print('escolha 5 para ESPONENCIAÇÃO')
print('escolha 6 para DIVISÃO INTEIRA')
print('escolha 7 para MODULO')
escolha = int(input('Digite o número da operação'))

if escolha == 1 :
        print('O resultado da soma entre {num1} e {num2} é: ', operação.soma())
elif escolha == 2 :
        print('O resultado da subtração entre {num1} e {num2} é: ', operação.subtraçãoo())
elif escolha == 3 :
        print('O resultado da multiplicação entre {num1} e {num2} é: ', operação.multiplicação())
elif escolha == 4 :
        print('O resultado da divisão entre {num1} e {num2} é: ', operação.divisão())
elif escolha == 5 :
        print('O resultado da exponenciação entre {num1} e {num2} é: ', operação.exponenciação())
elif escolha == 6 :
        print('O resultado da divisão inteira entre {num1} e {num2} é: ', operação.divisão_interia())
elif escolha == 7 :
        print('O resultado do modulo entre {num1} e {num2} é: ', operação.modulo())
else:
        print ('Operação invalida')