#1

class range:
    frase_fornecida =  "Instituto Federal de Santa Catarina"
    print("Vertical: \n")
    for cada_letra_da_frase in frase_fornecida:
        print(" ", cada_letra_da_frase)
    print(" ")
    print("Horizontal:")
    for item_da_lista in "Instituto Federal de Santa Catarina":
        palavra_na_horizontal = ""
    for item_da_lista in "Instituto Federal de Santa Catarina":
        palavra_na_horizontal = palavra_na_horizontal + item_da_lista
    print("\n" + palavra_na_horizontal)
    print("")

#2    
    print("Números pares de 0 a 20:")
    for numeros_de_0_a_20 in range(0,21, 2):
        print("->", numeros_de_0_a_20)
  
#3
    tabuada_escolhida_pelo_usuario = int(input("Qual tabuada você gostaria de ver?: ")) 
    
    for numero_da_tabuada in range (0,11):
        print(f"{numero_da_tabuada} x {tabuada_escolhida_pelo_usuario} = {numero_da_tabuada * tabuada_escolhida_pelo_usuario}")
        
#4  
    import time
    numeros_regressivos_20 = 0
    print("Contagem regressiva de 20 segundos: ")
    for numeros_regressivos_20 in range(1, 21):
        print(" ", numeros_regressivos_20)
        time.sleep(1)
        
#5  CORRIJIR
    print("Números de 1 a 100: ")
    
    for numeros_de_0_a_100 in range(1, 101):
        print("-> ", numeros_de_0_a_100)
    print("Números ímpares de 1 a 100: ")
    
    for numeros_de_0_a_100 in range (1, 100, 2):
        if numeros_de_0_a_100 % 2 == 1:
            print("-> ", numeros_de_0_a_100)
        
#6 CORRIJIR!
    numero_a_ser_lido = int(input("Digite um número qualquer: "))
   
    primo = True
    if numero_a_ser_lido % 2 == 0:    
        primo = False        
    if primo:
        print(f"O número {numero_a_ser_lido} é primo!")     
    else:
        print(f"O número {numero_a_ser_lido} não é primo!")
      
#7 
    frase_palindromo = str(input("Digite alguma frase: "))
    if frase_palindromo == frase_palindromo[::-1]: 
        print(f"{frase_palindromo}É um palíndromo!") 
    else: print(f"{frase_palindromo}Não é um palíndromo!")
    
#8 FAZER!

#9 CORRIJIR!
    letra = ""
    frase_inserida_pelo_usuario = str(input("Digite uma frase: "))
    if any (letra.islower()):
        print(" ", letra)
