#Kauã Marcos Malagutti
#David Junior Da Silva 
lista_dos_eventos=[]
quantidade_de_pessoas=[]
def cadastrar_eventos(titulo_do_evento,quantidade_maxima_de_pessoas):
    lista_dos_eventos.append(titulo_do_evento)
    quantidade_de_pessoas.append(quantidade_maxima_de_pessoas)
    print(f"O evento '{titulo_do_evento}' foi adicionado!\nSeu evento tem a quantidade maxima de {quantidade_maxima_de_pessoas} pessoas")
    return lista_dos_eventos, quantidade_de_pessoas 


def cadastrar_alunos(Cadastrar_novo_aluno):
    nome_alunos=[]
    nome_alunos.append(Cadastrar_novo_aluno)
    print(f"Conta do aluno {Cadastrar_novo_aluno} foi registrado ")
    return nome_alunos

def exibir_eventos(lista_dos_eventos, quantidade_de_pessoas):
    print(f"Eventos disponiveis: {lista_dos_eventos}\n{quantidade_de_pessoas}")
    return
    
def escreveraluno():
    return

def exibir_alunos_no_evento():
    return

#função principal
def menu_opcoes(): 
    while True:
        Menu_opcoes_escolher=input("DIgite um numero para as seguintes funções\n1= Cadastrar novo evento\n2=Cadastrar alunos\n3=Exibir eventos na tela\n4=fazer inscrição do aluno em um evento\n5=Exibir alunos no enento\n0=Para sair do Menu\nEscolha a opção desejada:   ")
        if Menu_opcoes_escolher =="1":
            titulo_do_evento=input("Insira o nome para o novo evento:   ")
            while True:
                    quantidade_maxima_de_pessoas=input("Insira a quantidade maxima de pessoas para seu novo evento: ")
                    if not quantidade_maxima_de_pessoas.isnumeric():
                        print("Favor inserir um numero valido!!\n")
                    else:
                        quantidade_maxima_de_pessoas=int(quantidade_maxima_de_pessoas)
                        Menu_opcoes_novo=Menu_opcoes_escolher
                        cadastrar_eventos(titulo_do_evento,quantidade_maxima_de_pessoas)
                        dados_cadastrar_evento=cadastrar_eventos
                        break
        elif Menu_opcoes_escolher=="2":
            Cadastrar_novo_aluno=input("Insira o nome do Estudante")
            cadastrar_alunos(Cadastrar_novo_aluno)
              
        elif Menu_opcoes_escolher=="3":
            exibir_eventos(lista_dos_eventos, quantidade_de_pessoas)
            
        elif Menu_opcoes_escolher=="4":
            escreveraluno()
            
        elif Menu_opcoes_escolher=="5":
            exibir_alunos_no_evento()
            
        elif Menu_opcoes_escolher=="0":
            deseja_sair=input("para sair, digite SAIR!\n    ").lower()
            if deseja_sair=='sair':
                break
        else: 
            print("Você continuou no programa!\n\n")
           
menu_opcoes()