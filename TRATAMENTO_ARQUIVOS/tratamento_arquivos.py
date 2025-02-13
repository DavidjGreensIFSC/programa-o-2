#David

import os

#arquivo evento.txt     - armazenar informações sobre o evento
#arquivo aluno.txt      - armazenar informações sobre o aluno
#arquivo inscricoes.txt - armazenar informações sobre a inscrição
ARQUIVO_EVENTO     = "evento.txt"
ARQUIVO_ALUNO      = "aluno.txt"
ARQUIVO_INSCRICOES = "inscricoes.txt"

SOMAR     = "SOMAR"
SUBTRAIR  = "SUBTRAIR"

eventos    = {} #dicionário para armazenar eventos. keys: título, capacidade, vagas restantes
alunos     = {} #dicionário para armazenar alunos. keys: nome, curso, instituição
inscricoes = {} #dicionário para armazenar as inscrições. keys: evento_nome, aluno_nome

#listas para armazenar informações de eventos alunos e inscrições
eventos_cadastrados  = []
alunos_cadastrados   = []
inscricoes_efetuadas = []


def menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Cadastrar evento")
    print("2. Excluir evento")
    print("3. Cadastrar aluno")
    print("4. Excluir aluno")
    print("5. Eventos disponíveis")
    print("6. Alunos cadastrados")
    print("7. Inscrever aluno em evento")
    print("8. Resumo final da SNCT")
    print("9. Sair")
    
   
def arquivoExistente(nomeArquivo):
    try:
        #o parâmentro 'nomeArquivo' deverá conter o caminho 'absoluto ou relativo' do arquivo, seu nome e sua extensão
        if (os.path.exists(nomeArquivo)):
            return True
        else:
            return False
    
    except Exception as erroArquivo:
        print(f"Erro: {erroArquivo}")     
        return False
    

def cadastrar_evento_arquivo():
    titulo     = input('\nDigite o nome do evento: ').strip()
    capacidade = input('Digite a capacidade máxima do evento: ').strip()
    #vagas = input("").strip()
    
    try:
        diretoriaAtualPasta = "" + os.getcwd() + "/" + ARQUIVO_EVENTO + ""
        #se o arquivo existe, abre no modo append, ou seja, adicionar conteúdo ao final do arquivo
        if arquivoExistente(diretoriaAtualPasta):
            fEvento = open(ARQUIVO_EVENTO, "a")
        else:
            #o arquivo não existe, e será aberto no modo write, ou seja, um arquivo em branco sem conteúdo
            fEvento = open(ARQUIVO_EVENTO, "w")
            #escreve na primeira linha o nome das colunas que identifica as informações
            nomeColunas = "Nome do Evento, Capacidade, Vagas restantes\n"
            fEvento.write(nomeColunas)
            
        linha = [titulo,
                 ",",
                 capacidade,
                 ",",
                 capacidade,
                 "\n"]

        informacoes = " ".join(linha)
        
        fEvento.write(f"{informacoes}")
        
        fEvento.close()
    
    except Exception as erroArquivo:
        print(f"Erro: {erroArquivo}")
        
        
def exibir_eventos_arquivo():
    try:
        fEvento = open(ARQUIVO_EVENTO, "r")
        
        for eventoArquivo in fEvento:
            registroEvento = eventoArquivo.split(",")
            print(registroEvento)
            
        fEvento.close()
        
    except Exception as erroArquivo:
        print(f"Erro ao ler arquivo: {erroArquivo}")
    
   
def atualizar_vagas(nomeEvento, tipoAtualizacao):
    msg = ''

    if len(eventos_cadastrados) > 0:
        for indice in range(len(eventos_cadastrados)):
            if eventos_cadastrados[indice].get('titulo').upper() == nomeEvento.upper():
                if tipoAtualizacao == SOMAR:
                    atualizar = int(eventos_cadastrados[indice].get('vagas_restantes')) + 1
                else:
                    atualizar = int(eventos_cadastrados[indice].get('vagas_restantes')) - 1
                
                #validar o numero máximo de vagas definida na criação do evento novo
                if atualizar >= 0:
                    eventos_cadastrados[indice].update({'vagas_restantes': atualizar})
                    msg = 'O evento ' + eventos_cadastrados[indice].get('titulo') + ' foi atualizado com sucesso!'
                else:
                    msg = 'Não há mais vagas disponíveis neste curso'
    else:
        msg = 'Não existem eventos cadastrados.'

    return msg


'''def cadastrarEvento(titulo, capacidade):
    if len(eventos_cadastrados) > 0:
        for indiceEvento in range(len(eventos_cadastrados)):
            if eventos_cadastrados[indiceEvento].get("titulo").upper() == titulo.upper():
                #encontrou o evento já cadastrado
                nomeEvento = eventos_cadastrados[indiceEvento].get("titulo")
                print(f"O evento {titulo} já foi cadastrado!")
                return
               
    try:
        eventos = {"titulo": titulo, 
                   "capacidade": capacidade,
                   "vagas_restantes": capacidade}
        print(f"\nO evento '{tituloEvento}' foi cadastrado!")
        
        #armazena eventos na lista de eventos
        eventos_cadastrados.append(eventos)            
    except ValueError: 
        print("\nCapacidade inválida!")'''


'''def excluirEvento(tituloEventoExcluir): 
    if len(eventos_cadastrados) <= 0:
        print("\nNão existem eventos cadastrados para serem excluídos.")
        return
    else:
        for indiceEvento in range(len(eventos_cadastrados)):
            if eventos_cadastrados[indiceEvento].get("titulo").upper() == tituloEventoExcluir.upper():
                #encontrou o evento a ser excluído
                
                print(f"Índice do evento a ser excluido é = {indiceEvento}")
                
                eventos_cadastrados.pop(indiceEvento)
                print(f"O evento {tituloEventoExcluir} foi excluido com sucesso.")
                break'''


def excluirEvento(nomeEvento):
    registroArquivo = []
    
    try:
        diretorioAtualPasta = "" + os.getcwd() + "/" + ARQUIVO_EVENTO + ""     
      
        if arquivoExistente(diretorioAtualPasta): 
            #o arquivo OBRIGATORIAMENTE deverá ser aberto no modo leitura
            with open(diretorioAtualPasta, "r") as arquivoDeEventos:
                registroArquivo = arquivoDeEventos.readlines() #para ler todas as linhas de uma vez            
                
            if(len(registroArquivo) > 0):
                
                for indiceLinha in range(len(registroArquivo)):
                    linha = registroArquivo[indiceLinha]
                        
                    if linha.find(nomeEvento) >= 0:
                        #encontrou o evento e exclui da lista de eventos
                        registroArquivo.pop(indiceLinha)
            
            #trunca (zera, apaga) o arquivo e copia a lista para dentro do arquivo       
            if(len(registroArquivo) > 0):
                with open(diretorioAtualPasta, "w") as arquivoDeEventosAlterado:
                    arquivoDeEventosAlterado.writelines(registroArquivo)
                   
        else:
            print("Não há eventos para serem excluídos")
        
    except Exception as erroArquivo:
        print(f"Erro na manipulação de arquivo {erroArquivo}")



def cadastrarAluno(nomeAluno, curso, instituicao):
    if len(alunos_cadastrados) > 0:
        for indiceAluno in range(len(alunos_cadastrados)):
            if alunos_cadastrados[indiceAluno].get("nome").upper() == nomeAluno.upper():
                #encontrou o aluno já cadastrado
                nomeAluno = alunos_cadastrados[indiceAluno].get("nome")
                print(f"O aluno {nomeAluno} já foi cadastrado!")
                return
           
    try:
        alunos = {"nome": nomeAluno, 
                   "curso": curso,
                   "instituicao": instituicao}
        print(f"\nO aluno '{nomeAluno}' foi cadastrado!")
        
        #armazena aluno na lista de alunos
        alunos_cadastrados.append(alunos)  
 
    except ValueError: 
        print("\nFalha no cadastro do aluno!")
    

def excluirAluno(nomeAlunoExcluir):
    if len(alunos_cadastrados) <= 0:
        print(f"\nNão existem alunos cadastrados para serem excluídos.")
        return
    else:
        for indiceAluno in range(len(alunos_cadastrados)):
            if alunos_cadastrados[indiceAluno].get("nome").upper() == nomeAlunoExcluir.upper():
                #encontrou o evento a ser excluído
                
                alunos_cadastrados.pop(indiceAluno)
                print(f"\nO aluno {nomeAlunoExcluir} foi excluído com sucesso.")
                break


def exibirAlunos():
    if len(alunos_cadastrados) <= 0:
        print("\nNenhum aluno cadastrado.")
        return
    else:
        for indiceAluno in range(len(alunos_cadastrados)):
            nomeAluno   = alunos_cadastrados[indiceAluno].get("nome")
            curso       = alunos_cadastrados[indiceAluno].get("curso")
            instituicao = alunos_cadastrados[indiceAluno].get("instituicao")
            print(f"Aluno: {nomeAluno} | Curso: {curso} | Instituição: {instituicao}")
    
    
'''def exibirEventos():
    if len(eventos_cadastrados) <= 0:
        print("\nNenhum evento cadastrado.")
        return
    else:
        for indiceEvento in range(len(eventos_cadastrados)):
            nomeEvento     = eventos_cadastrados[indiceEvento].get("titulo")
            capacidade     = eventos_cadastrados[indiceEvento].get("capacidade")
            vagasRestantes = eventos_cadastrados[indiceEvento].get("vagas_restantes")
            print(f"Evento: {nomeEvento} | Capacidade: {capacidade} | Vagas restantes: {vagasRestantes}")'''
    

def inscreverAluno(nomeAlunoInscricao, tituloEventoInscricao):
    exibir_eventos_arquivo()
    if len(inscricoes_efetuadas) > 0:
        nomeEvento = ""
        nomeAluno  = ""
        
        for indiceInscricao in range(len(inscricoes_efetuadas)):
            nomeEvento = inscricoes_efetuadas[indiceInscricao].get("evento_nome").upper()
            nomeAluno  = inscricoes_efetuadas[indiceInscricao].get("aluno_nome").upper()
            
            if (nomeEvento == tituloEventoInscricao) & (nomeAluno == nomeAlunoInscricao):
                #aluno já cadastrado no evento 
                print(f"O aluno {nomeAlunoInscricao} já está inscrito no evento {tituloEventoInscricao}!")
                return
            #keys: evento_nome, aluno_nome
    
    try:
        #dicionário inscrições
        inscricoes = {"evento_nome": tituloEventoInscricao, 
                      "aluno_nome": nomeAlunoInscricao}
        
        #armazena inscrição na lista de inscrições
        inscricoes_efetuadas.append(inscricoes)  
        
        print(f"\nO aluno '{nomeAlunoInscricao}' foi inscrito no evento {tituloEventoInscricao} com sucesso!")
        
        #atualiza o número de vagas restantes do evento
        atualizar_vagas(tituloEventoInscricao, SUBTRAIR)     
        
    except ValueError: 
        print("\nFalha no cadastro da inscrição!")


def exibirResumo():
    print("\n---- Resumo Final da SNCT ----")
    for evento in eventos_cadastrados:
        tituloEvento = evento["titulo"]
        participantes = sum(1 for inscricao in inscricoes_efetuadas if inscricao["evento_nome"] == tituloEvento)
        print(f"Evento: {tituloEvento} | Participantes: {participantes}")
        


while True:
    menu()
    opcao = input("Digite o número correspondente a opção que deseja escolher: ")
    
    if opcao == "1":
        #cadastrarEvento(tituloEvento, capacidade)
        cadastrar_evento_arquivo()
        
    elif opcao == "2": # Exibir 1eventos cadastrados.
        exibir_eventos_arquivo()
        nomeEvento = input("\nDigite o título do evento a ser excluído: ")
        excluirEvento(nomeEvento)
        
    elif opcao == "3":
        nomeAluno   = input("\nDigite o nome do aluno que deseja cadastrar: ")
        cursoAluno  = input("Informe o curso do aluno: ")
        instituicao = input("Informe a instituição que o aluno estuda: ")
        cadastrarAluno(nomeAluno, cursoAluno, instituicao)
        
    elif opcao == "4":
        nomeAlunoExcluir = input("\nDigite o nome do aluno a ser excluído: ")
        excluirAluno(nomeAlunoExcluir)
        
    elif opcao == "5":
        exibir_eventos_arquivo()

    elif opcao == "6":
        exibirAlunos()
        
    elif opcao == "7":
        exibir_eventos_arquivo()
        tituloEventoInscricao = input("\nDigite o título do evento escolhido: ")
        nomeAlunoInscricao    = input("Digite o nome do aluno: ")
        inscreverAluno(nomeAlunoInscricao, tituloEventoInscricao)
        
    elif opcao == "8":
        exibirResumo()
        
    elif opcao == "9":
        print("\nEncerrando o programa...")
        break
    
    else:
        print("\nOpção inválida! Tente novamente.")
        