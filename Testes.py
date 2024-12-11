from colorama import init, Fore
init()

lista_dos_eventos = []
quantidade_de_pessoas = []
alunos_por_evento = {}

def cadastrar_eventos(titulo_do_evento, quantidade_maxima_de_pessoas):
    lista_dos_eventos.append(titulo_do_evento)
    quantidade_de_pessoas.append(quantidade_maxima_de_pessoas)
    alunos_por_evento[titulo_do_evento] = []
    print(Fore.GREEN + f"O evento '{titulo_do_evento}' foi adicionado!" + Fore.RESET)
    print(Fore.GREEN + f"Seu evento tem a quantidade máxima de {quantidade_maxima_de_pessoas} pessoas." + Fore.RESET)

def cadastrar_alunos(nome_aluno):
    print(Fore.GREEN + f"O(a) aluno(a) {nome_aluno} foi registrado no sistema!" + Fore.RESET)
    return nome_aluno

def exibir_eventos():
    print(Fore.LIGHTYELLOW_EX + "Eventos disponíveis:" + Fore.RESET)
    for evento, vagas in zip(lista_dos_eventos, quantidade_de_pessoas):
        print(f"- {evento}: {vagas} vaga(s) disponível(is)")

def fazer_inscricao(aluno, evento):
    if evento not in lista_dos_eventos:
        print(Fore.RED + "Evento não encontrado." + Fore.RESET)
        return

    indice_evento = lista_dos_eventos.index(evento)

    if quantidade_de_pessoas[indice_evento] <= 0:
        print(Fore.RED + "O número de participantes nesse evento foi excedido." + Fore.RESET)
        return

    alunos_por_evento[evento].append(aluno)
    quantidade_de_pessoas[indice_evento] -= 1
    print(Fore.GREEN + f"O(a) aluno(a) {aluno} foi inscrito(a) no evento '{evento}'." + Fore.RESET)

def exibir_alunos_no_evento():
    print(Fore.LIGHTYELLOW_EX + "Alunos por evento:" + Fore.RESET)
    for evento, alunos in alunos_por_evento.items():
        print(f"- {evento}: {', '.join(alunos) if alunos else 'Nenhum aluno inscrito.'}")

def menu_opcoes():
    while True:
        Menu_opcoes_escolher = input("\nDigite um número para as seguintes funções:\n"
                                    "1 = Cadastrar novo evento\n"
                                    "2 = Cadastrar aluno\n"
                                    "3 = Exibir eventos na tela\n"
                                    "4 = Fazer inscrição do aluno em um evento\n"
                                    "5 = Exibir alunos no evento\n"
                                    "Digite 'sair' para sair do menu\n"
                                    "Escolha a opção desejada: ").strip().lower()

        if Menu_opcoes_escolher == "1":
            titulo_do_evento = input("Insira o nome para o novo evento: ").strip()
            while True:
                quantidade_maxima_de_pessoas = input("Insira a quantidade máxima de pessoas para seu novo evento: ").strip()
                if not quantidade_maxima_de_pessoas.isnumeric():
                    print(Fore.RED + "Favor inserir um número válido!" + Fore.RESET)
                else:
                    quantidade_maxima_de_pessoas = int(quantidade_maxima_de_pessoas)
                    cadastrar_eventos(titulo_do_evento, quantidade_maxima_de_pessoas)
                    break

        elif Menu_opcoes_escolher == "2":
            nome_aluno = input("Insira o nome do estudante: ").strip()
            cadastrar_alunos(nome_aluno)

        elif Menu_opcoes_escolher == "3":
            exibir_eventos()

        elif Menu_opcoes_escolher == "4":
            nome_aluno = input("Insira o nome do aluno para inscrição: ").strip()
            evento = input("Insira o nome do evento: ").strip()
            fazer_inscricao(nome_aluno, evento)

        elif Menu_opcoes_escolher == "5":
            exibir_alunos_no_evento()

        elif Menu_opcoes_escolher == "sair":
            deseja_sair = input("Tem certeza que deseja sair? Digite 'sair' novamente para confirmar: ").strip().lower()
            if deseja_sair == 'sair':
                break

        else:
            print(Fore.RED + "Por favor, selecione uma opção válida!" + Fore.RESET)

menu_opcoes()
