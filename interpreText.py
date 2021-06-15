from time import sleep

titulos = list()    #Listas e Dicionarios
temas = list()
cadastro = dict()
historia = dict()
historias = list()
questoes = dict()
listaQuestoes = list()
listProfessores = list()
listAlunos = list()
prof = dict()
aluno = dict()

#FUNÇÕES DOS PROFESSORES
def linha(tam=42):      #Função para criar uma linha
    return '-' * tam


def cadTemas():     #Cadastrar Temas
    try:
        tema = str(input('\033[1;30mDigite o tema: \033[m')).capitalize()
        if tema not in temas:
            temas.append(tema)
            print('\033[1;30mTema\033[m \033[1;32m{}\033[m armazenado!\033[m'.format(tema))
    except (ValueError, TypeError):
        print('\033[1;30mErro na leitura dos temas!\033[m')
    return temas


def cadHistorias(tema, titulo, historias): #Cadastrar histórias
    try:
        historia.clear()
        historia['tema'] = tema
        historia['titulo'] = titulo
        historia[titulo] = str(input('\033[1;30mEntre com a historia: \033[m')) #Cada historia vai ser um dicicionario dentro de uma lista
        historias.append(historia.copy())
        print('\033[1;32mHistoria armazenada!\033[m')
    except (ValueError, TypeError):
        print("\033[1;31mErro na leitura das histórias!\033[m")
    return historias


def mostrarTitulo(historias): #Mostra titulo das histórias disponiveis
    print('\033[1;30mAs historias cadastradas foram: \n\033[m')
    for historia in historias:
        print(f'\033[1;34m{historia["titulo"]} \033[m')


def lerHistoria(historias): #Mostra a história
    mostrarTitulo(historias)
    titulo = input("\033[1;30mDigite o titulo da historia a ser lida: \033[m")
    print()
    print('\033[1;30mA historia escolhida foi: \n\033[m')
    print(f'\033[1;34m{titulo} \n\033[m')
    for historia in historias:
        if (historia['titulo'] == titulo):
            print()
            print(f'{historia[titulo]} \n\n')


def apagarHistoria(historias): #Apagar uma história
    mostrarTitulo(historias)
    titulo = str(input("\033[1;30mQual a historia que voce deseja apagar?   \033[m"))
    apagada = False
    for historia in historias:
        if (historia['titulo'] == titulo):
            historias.remove(historia)
            apagada = True
            break
    if apagada:
        print(f"\033[1;32mHistória {titulo} apagada! \033[m")
    else:
        print(f"\033[1;31mHistória {titulo} não encontrada! \033[m")


def printTemas(temas):  #Mostra os temas cadastrados
    print('\033[1;30mTemas cadastrados: \033[m')
    if (len(temas) == 0):
        print("\033[1;31mNao existem temas cadastrados\033[m")
    for tema in temas:
        print(tema)


def criarQuestoes(titulo):  #Cria questões
    questoes = dict()       #Dicionario Principal, uma chave
    perguntas = dict()
    pergunta1 = dict()      #Dicionario secundario
    respostas1 = dict()

    pergunta2 = dict()
    respostas2 = dict()

    pergunta3 = dict()
    respostas3 = dict()

    pergunta4 = dict()
    respostas4 = dict()

    pergunta5 = dict()
    respostas5 = dict()

    pergunta1['pergunta'] = str(input("\033[1;30mEntre com a primeira pergunta: \033[m"))
    sleep(0.3)

    print('Digite 5 respostas: ')

    respostas1['a'] = str(input("\033[1;30mEntre com a resposta a: \033[m"))
    respostas1['b'] = str(input("\033[1;30mEntre com a resposta b: \033[m"))
    respostas1['c'] = str(input("\033[1;30mEntre com a resposta c: \033[m"))
    respostas1['d'] = str(input("\033[1;30mEntre com a resposta d: \033[m"))
    respostas1['e'] = str(input("\033[1;30mEntre com a resposta e: \033[m"))
    sleep(0.3)

    pergunta1['respostas'] = respostas1
    pergunta1['resposta_certa'] = str(input("\033[1;30mEntre com o item da resposta certa: \033[m"))
    perguntas['Pergunta 1'] = pergunta1

    ############################ Pergunta 2 #######################################

    pergunta2['pergunta'] = input('Entre com a pergunta 2: ')
    sleep(0.3)

    print('Digite 5 respostas: ')

    respostas2['a'] = str(input("Entre com a resposta a: "))
    respostas2['b'] = str(input("Entre com a resposta b: "))
    respostas2['c'] = str(input("Entre com a resposta c: "))
    respostas2['d'] = str(input("Entre com a resposta d: "))
    respostas2['e'] = str(input("Entre com a resposta e: "))
    sleep(0.3)

    pergunta2['respostas'] = respostas2
    pergunta2['resposta_certa'] = str(input("Entre com o item da resposta certa: "))
    perguntas['Pergunta 2'] = pergunta2

    ########################### Pergunta 3 #######################################

    pergunta3['pergunta'] = input('Entre com a pergunta 3: ')
    sleep(0.3)
    print('Digite 5 respostas: ')

    respostas3['a'] = str(input("Entre com a resposta a: "))
    respostas3['b'] = str(input("Entre com a resposta b: "))
    respostas3['c'] = str(input("Entre com a resposta c: "))
    respostas3['d'] = str(input("Entre com a resposta d: "))
    respostas3['e'] = str(input("Entre com a resposta e: "))
    sleep(0.3)
    pergunta3['respostas'] = respostas3
    pergunta3['resposta_certa'] = str(input("Entre com o item da resposta certa: "))
    perguntas['Pergunta 3'] = pergunta3
    #
    # ############################ Pergunta 4 #######################################
    #
    # pergunta3['pergunta'] = input('Entre com a pergunta 4: ')
    #
    # print('Digite 5 respostas: ')
    #
    # respostas4['a'] = str(input("Entre com a resposta a: "))
    # respostas4['b'] = str(input("Entre com a resposta b: "))
    # respostas4['c'] = str(input("Entre com a resposta c: "))
    # respostas4['d'] = str(input("Entre com a resposta d: "))
    # respostas4['e'] = str(input("Entre com a resposta e: "))
    #
    # pergunta4['respostas'] = respostas4
    # pergunta4['resposta_certa'] = str(input("Entre com o item da resposta certa: "))
    # perguntas['Pergunta 4'] = pergunta4
    #
    # ############################ Pergunta 4 #######################################
    #
    # pergunta5['pergunta'] = input('Entre com a pergunta 5: ')
    #
    # print('Digite 5 respostas: ')
    #
    # respostas5['a'] = str(input("Entre com a resposta a: "))
    # respostas5['b'] = str(input("Entre com a resposta b: "))
    # respostas5['c'] = str(input("Entre com a resposta c: "))
    # respostas5['d'] = str(input("Entre com a resposta d: "))
    # respostas5['e'] = str(input("Entre com a resposta e: "))
    #
    # pergunta5['respostas'] = respostas5
    # pergunta5['resposta_certa'] = str(input("Entre com o item da resposta certa: "))
    # perguntas['Pergunta 5'] = pergunta5

    questoes[titulo] = perguntas
    listaQuestoes.append(questoes.copy())

    return listaQuestoes


def leiaInt(msg):  #Validação de um inteiro
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


def cabecalho(txt): #Cabecalho
    print(linha())
    print(txt)
    print(linha())


def menu(lista):    #Menu principal dos professores
    cabecalho('\033[1;35mMENU PRINCIPAL\033[m')
    for c, iten in enumerate(lista):
        sleep(0.3)
        print(f'\033[1;30m{c + 1} - \033[m\033[1;36m{iten}\033[m')

    print(linha())
    opc = leiaInt('\033[1;30mSua Opcao: \033[m')
    return opc


#FUNÇÕES ALUNOS

# recebe as histórias como parâmetro
def verificarTemas(historias):      #Verifica se um tema é repetido e adiciona na lista
    temaAleatorio = set() #Cria o set
    for historia in historias:
        temaAleatorio.add(historia['tema'])  # o set já verifica se o elemento é repetido

    temaAleatorio = list(temaAleatorio)  # transforma o set em lista, pois set's não tem ordem definida
    for i, tema in enumerate(temaAleatorio, start=1):  # MOSTRA TEMAS
        print(f' \033[1;30m{i} -\033[m \033[1;36m{tema}\033[m')
        sleep(0.3)
    return temaAleatorio  # retorna a lista de temas


def leiaOpcao(historias, listaQuestoes):
    dicionario = dict()
    while True:  # enquanto a escolha não for válida, pede que digite novamente
        try:
            escolha = int(
                input(('\033[1;30mDigite o número que está relacionado com o tema a sua escolha: \033[m')))
            print()
            if 1 <= escolha <= len(temaAleatorio):                      #Pede pro usuário escolher o tema
                break  # escolha válida, sai do while
            else:
                print(f'\033[1;31mNúmero deve estar entre 1 e {len(temaAleatorio)}\033[m')
        except ValueError:  # se não digitar número, dá erro
            print('\033[1;31mDigite um número válido\033[m')

    cont = 0
    tema_escolhido = temaAleatorio[escolha - 1]
    for historia in historias:

        if historia['tema'] == tema_escolhido:  # Se a história tem o tema escolhido
            cont += 1

    if cont > 0:
        print('\033[1;30mTítulos das histórias do tema escolhido:\033[m')
        for historia in historias:
            if historia['tema'] == tema_escolhido:                                 #Aparece os titulos do tema escolhido
                titulo = historia['titulo']
                print(f'\033[1;34m{titulo}\033[m')
                sleep(0.5)

    print()

    sair = 0
    while sair == 0:
        try:
            titulo = input('\033[1;30mDigite a história você deseja ler e responder as questões: \033[m')

            for historia in historias:
                if historia['titulo'] == titulo:                                    #Pede pra escolher entre os titulos do tema
                    print()
                    print(f'{historia[titulo]} \n\n')
                    sair = 1
        except:
            print('\033[1;30mO título que digitou não existe!\033[m')

#QUESTÕES

    for i in range(len(listaQuestoes)):         #Quais questões são do titulo que ele escolheu
        if titulo in listaQuestoes[i]:              #Vai relacionar as questões ao respectivo titulo
            dicionario = listaQuestoes[i]

    perguntas = dicionario[titulo]
    respostasCertas = 0

    for pk, pv in perguntas.items():  # Pk vai ser o numero da pergunta, pv vai ser a pergunta
        print(f'{pk}: {pv["pergunta"]}')

        print('\033[1;30mEscolha uma das opções: \033[m')
        for rk, rv in pv['respostas'].items():  # Rk - Simbolo da alternativa, rv - texto da alternativa
            print(f'[{rk}]: {rv}')
            sleep(0.3)

        sleep(3)
        respostaUsuario = input('\033[1;30mSua resposta: \033[m')
        if respostaUsuario == pv['resposta_certa']:
            sleep(0.3)
            print('\033[1;32mMuito bem! Você acertou.\033[m')
            respostasCertas += 1
        else:
            sleep(0.3)
            print('\033[1;31mErrou! Preste mais atenção!\033[m')
        print()

    quantPerguntas = len(perguntas)
    if quantPerguntas > 0:

        sleep(1)
        porcentagemAcerto = respostasCertas / quantPerguntas * 100      #Porcentagem do total de acertos
        print(f'\033[1;30mVocê acertou  {respostasCertas} resposta(s).\033[m')
        print(f'\033[1;30mSua porcentagem foi {porcentagemAcerto}%\033[m')
        sleep(0.5)

    else:
        sleep(1)
        print('\033[1;31mInfelizmente você não acertou nenhuma resposta!\033[m')


#FUNÇÕES CADASTRAMENTO


def cadastrarProfessor():   # Cadastrar o professor

    prof['nomeProfessor'] = input('\033[1;30mDigite o nome do professor que você deseja cadastrar: \033[m')
    prof['matriculaProfessor'] = input('\033[1;30mDigite a matricula do professor: \033[m')
    prof['senhaProfessor'] = input('\033[1;30mDigite a senha do professor: \033[m')

    listProfessores.append(prof.copy())
    return listProfessores


def cadAdm():       #Cadastra os admin
    inicio = 0
    if inicio == 0:

        nomeAdm = input('\033[1;30mDigite o seu primeiro nome: \033[m')
        senhaAdm = input('\033[1;30mCadastre uma senha: \033[m')
        inicio = 1
        sleep(1)
        print('\033[1;32mCadastrado como administrador do programa!!\033[m')

    cont = 3
    while cont > 0:
        sleep(0.5)
        senha = input('\033[1;30mDigite sua senha de administrador para acessar o programa: \033[m')
        if (senhaAdm == senha):
            erro = 1
            while erro == 1:
                try:
                    esc = input('\033[1;30mCadastrar matricula de um professor? [Sim/Nao] \033[m').strip().lower()[0]
                    erro = 0
                except:
                    print('\033[1;31mDigite Sim ou Não!\033[m')

            while esc == 's':
                cadastrarProfessor()
                sleep(0.5)
                print('\033[1;32mCadastrado com sucesso!\033[m')
                sleep(0.5)
                erro = 1
                while erro == 1:
                    try:
                        esc = input('\033[1;30mCadastrar nova matricula? [Sim/Nao] \033[m').strip().lower()[0]
                        erro = 0
                    except:
                        print('\033[1;31mDigite sim ou não!\033[m')
            break
        else:
            cont -= 1
            print(f'\033[1;31mVocê tem {cont} chances.\033[m')


def cadastrarUsuarios(): #Chama as funções de cadastro e também realiza cadastros
    op = -1
    aluno = dict()

    while op != 0:

        linha(42)
        print('\033[1;30m1 - \033[m\033[1;36mLogin Admin\033[m')
        sleep(0.3)
        print('\033[1;30m2 - \033[m\033[1;36mLogin Professor\033[m')
        sleep(0.3)
        print('\033[1;30m3 - \033[m\033[1;36mLogin Aluno\033[m')
        sleep(0.3)
        print('\033[1;31m0 - SAIR\033[m')
        sleep(0.3)

        while op != 0:
            try:
                op = int(input(('\033[1;30mDigite a sua opção: \033[m'))) #Validação para ser um int como entrada
                break
            except ValueError:  # se não digitar número, dá erro
                print('\033[1;31mDigite um número válido\033[m')

        if op == 1: #Se for 1, cadastra o admin

            cadAdm()

        elif op == 2:   #Se for 2, loga o professor

            matricula = input('\033[1;30mDigite sua matricula: \033[m')
            for i in range(len(listProfessores)):
                if matricula in listProfessores[i]['matriculaProfessor']:
                    cont = 3
                    while cont > 0:
                        senha = input('\033[1;30mDigite sua senha: \033[m')
                        if senha in listProfessores[i]['senhaProfessor']:

                            print('\033[1;32mLogado com sucesso!\033[m')
                            op = 2
                            return op
                        else:
                            cont -= 1
                            print(f'Você tem {cont} chances.')

                    else:
                        print('\033[1;31mMatricula não encontrada. Por favor procure a coordenação.\033[m')
                else:
                    print('\033[1;31mMatricula não encontrada. Por favor procure a coordenação.\033[m')

        elif op == 3: #se for 3, cadastra ou loga o aluno

            erro = 1
            while erro == 1:
                try:
                    loginAluno = \
                    input('\033[1;30mDeseja se cadastrar ou logar? [Cadastrar/logar] \033[m').strip().lower()[
                        0]  # Strip tira os espaços antes e depois, lower minusculo e [0] pega a primeira letra
                    erro = 0
                except:
                    print('\033[1;31mOpção inválida!\033[m')

            if loginAluno == 'c':

                aluno['nome'] = input('\033[1;30mDigite o seu nome: \033[m')
                aluno['matricula'] = input('\033[1;30mDigite sua matricula: \033[m')
                senha1 = input('\033[1;30mDigite sua senha: \033[m')
                senha2 = input('\033[1;30mConfirme sua senha: \033[m')
                while senha1 != senha2:
                    print('\033[1;31mSenhas diferentes. Tente novamente!\033[m')
                    senha1 = input('\033[1;30mDigite sua senha: \033[m')
                    senha2 = input('\033[1;30mConfirme sua senha: \033[m')
                aluno['senha'] = senha2
                listAlunos.append(aluno.copy())
                print('\033[1;32mCadastrado com sucesso!\033[m')

            elif loginAluno == 'l':

                matricula = input('\033[1;30mDigite sua matricula: \033[m')
                if matricula.isnumeric():

                    for i in range(len(listAlunos)):

                        if matricula in listAlunos[i]['matricula']:
                            cont = 3
                            while cont > 0:
                                senha = input('\033[1;30mDigite sua senha: \033[m')
                                if senha in listAlunos[i]['senha']:

                                    print('\033[1;32mLogado com sucesso!\033[m')
                                    op = 3
                                    return op
                                else:
                                    cont -= 1
                                    print(f'\033[1;30mVocê tem {cont} chances.\033[m')

                            else:
                                print('\033[1;30mMatricula não encontrada. Por favor cadastre-se!\033[m')
                else:
                    print('\033[1;30mDigite número no campo.\033[m')

            else:
                print('\033[1;30mOpção Inválida! Tente Novamente!\033[m')

        elif op == 0:
            exit()

        else:
            print('\033[1;30mOpção invalida\033[m')
######################################## Programa Principal ########################################

#Chama as funções principais
op = -1
while (op != 0):
    op = cadastrarUsuarios()

    listaMenu = ['Cadastrar tema', 'Cadastrar historia', 'Mostrar titulos', 'Ler historia',
                 'Apagar historia', 'Mostrar temas', 'Criar questoes', 'Sair do Sistema']
    if op == 2:
        resposta = 1
        while (resposta != len(listaMenu)):
            resposta = menu(listaMenu)
            if (resposta == 1):
                cadTemas()

            elif (resposta == 2):
                printTemas(temas)
                sair = 0
                chances = 3
                while (chances > 0):
                    tema = str(input('\033[1;30mEntre com o tema: \033[m')).capitalize()
                    if (tema in temas):
                        break
                    print("\033[1;31mTema inexistente, por favor tente outra vez!\033[m")
                    chances -= 1
                    print(f'\033[1;31mVoce tem {chances} chances!\033[m')

                if (sair < 3):
                    titulo = str(input('\033[1;30mEntre com o titulo da historia: \033[m'))
                    cadHistorias(tema, titulo, historias)

            elif (resposta == 3):
                mostrarTitulo(historias)

            elif (resposta == 4):
                lerHistoria(historias)

            elif (resposta == 5):
                apagarHistoria(historias)

            elif (resposta == 6):
                printTemas(temas)

            elif (resposta == 7):
                mostrarTitulo(historias)
                titulo = str(input('\033[1;30mEntre com o titulo da historia: \033[m')) #validação aqui
                questoes = criarQuestoes(titulo)


            elif resposta == (len(listaMenu)):
                cabecalho('\033[1;30mSaindo do sistema... Ate logo!\033[m')

            else:
                print('\033[31mERRO! Digite uma opcao valida!\033[m')
                sleep(5)

    elif op == 3:

        temaAleatorio = verificarTemas(historias)

        leiaOpcao(historias, listaQuestoes)















