#Kauã Marcos Malagutti
#David Junior Da Silva 

"""Professor Alexandre, para executar o mosso código por favor instale a biblioteca Colorama na sua máquina!!!
Para isso abra um terminal separado e digite "pip install colorama", isso não necessário para o funcionamento do código mas 
a experiência de uso ficará melhor."""

from colorama import init, Fore, Back, Style
init()

lista_dos_eventos=[]
quantidade_de_pessoas=[]
def cadastrar_eventos(titulo_do_evento,quantidade_maxima_de_pessoas):
    lista_dos_eventos.append(titulo_do_evento)
    quantidade_de_pessoas.append(quantidade_maxima_de_pessoas)
    print(Fore.GREEN + f"O evento '{titulo_do_evento}' foi adicionado! " + Fore.RESET )
    print(Fore.GREEN + f"Seu evento tem a quantidade maxima de {quantidade_maxima_de_pessoas} pessoas" + Fore.GREEN)
    return lista_dos_eventos, quantidade_de_pessoas 


def cadastrar_alunos(Cadastrar_novo_aluno):
    nome_alunos=[]
    nome_alunos.append(Cadastrar_novo_aluno)
    print(Fore.GREEN + f"O(a) Aluno(a) {Cadastrar_novo_aluno} foi registrado no sistema! " + Fore.RESET)
    return nome_alunos

def exibir_eventos(lista_dos_eventos, quantidade_de_pessoas):
    print(Fore.LIGHTYELLOW_EX + f"Eventos disponiveis: {lista_dos_eventos}\n Número de vagas disponíveis: {quantidade_de_pessoas}" + Fore.RESET)
    return
    
def escreveraluno():
    return

def exibir_alunos_no_evento():
    return

#função principal
def menu_opcoes(): 
    while True:
        Menu_opcoes_escolher=input("Digite um número para as seguintes funções\n1 = Cadastrar novo evento\n2 = Cadastrar alunos\n3 = Exibir eventos na tela\n4 = fazer inscrição do aluno em um evento\n5 = Exibir alunos no enento\nDigite ''Sair'' para sair do Menu\nEscolha a opção desejada:   ")
        if Menu_opcoes_escolher =="1":
            titulo_do_evento=input("Insira o nome para o novo evento:   ")
            while True:
                    quantidade_maxima_de_pessoas=input("Insira a quantidade maxima de pessoas para seu novo evento: ")
                    if not quantidade_maxima_de_pessoas.isnumeric():
                        print(Fore.RED + "Favor inserir um numero valido!!\n" + Fore.RESET)
                    else:
                        quantidade_maxima_de_pessoas=int(quantidade_maxima_de_pessoas)
                        Menu_opcoes_novo=Menu_opcoes_escolher
                        cadastrar_eventos(titulo_do_evento,quantidade_maxima_de_pessoas)
                        dados_cadastrar_evento=cadastrar_eventos
                        break
        elif Menu_opcoes_escolher=="2":
            Cadastrar_novo_aluno=input("Insira o nome do Estudante: ")
            cadastrar_alunos(Cadastrar_novo_aluno)
              
        elif Menu_opcoes_escolher=="3":
            exibir_eventos(lista_dos_eventos, quantidade_de_pessoas)
            
        elif Menu_opcoes_escolher=="4":
            escreveraluno()
            
        elif Menu_opcoes_escolher=="5":
            exibir_alunos_no_evento()
            
        elif Menu_opcoes_escolher=="sair":
            deseja_sair=input("para sair, digite SAIR!\n    ").lower()
            if deseja_sair=='sair':
                break
        else: 
            print("Por favor, selecione uma opção válida!\n\n")
           
menu_opcoes()