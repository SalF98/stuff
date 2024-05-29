manifestacoes = []
opcao = 0

while opcao != 6:
    print("\nBem-Vindo ao Sistema de Satisfação ao Cliente!")
    print("Selecione o que fazer:")
    print("1) Listar Manifestações")
    print("2) Criar uma nova Manifestação")
    print("3) Exibir quantidade de manifestações")
    print("4) Pesquisar uma manifestação por código")
    print("5) Excluir uma Manifestação pelo Código")
    print("6) Sair do Sistema")

    opcao = int(input('Selecione uma opção: '))

    if opcao == 1:
        if len(manifestacoes) != 0:
            print('\nLista de Manifestações:')
            for quantidade in range(len(manifestacoes)):
                print(quantidade + 1, ')', manifestacoes[quantidade])
            print()
        else:
            print("\nA lista está vazia.\n")

    if opcao == 2:
        nomeNovaManifestacao = input("Digite o nome da manifestação: ")
        manifestacoes.append(nomeNovaManifestacao)
        print("Manifestacao adicionada com sucesso!")

    if opcao == 3:
        quantidadeManifestacoes = len(manifestacoes)
        print("Temos", quantidadeManifestacoes, "cadastradas no sistema")

    if opcao == 4:
        codigo = int(input("Digite o código da manifestação: "))
        if codigo > 0 and codigo <= len(manifestacoes):
            print("A manifestação pesquisada foi", manifestacoes[codigo - 1])
        else:
            print("Código informado inválido!")

    if opcao == 5:
        posicao = int(input("Digite a posição da manifestação que deseja remover: "))
        if 1 <= posicao <= len(manifestacoes):
            manifestacoes.pop(posicao - 1)
            print('Manifestação removida')
        else:
            print('Posição informada inválida')

print('Obrigado por usar o sistema!')



'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿
⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿        JESSE WE GOTTA COOK
⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿
'''
'''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠴⠒⠒⠛⠛⠓⠚⣻⣿⣗⣦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⣩⣴⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣷⣌⡙⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⣰⣾⣿⠟⠉⠉⠉⠉⠙⠟⣿⣿⣿⣿⣿⣿⡟⢦⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢋⣴⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠋⢿⣿⣿⣿⡃⠀⡀⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢏⣼⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣧⠀⢻⣆⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⣶⠈⢻⣿⡄⠸⡟⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠙⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡆⢸⣿⡇⠀⡁⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⠀⠀⣀⡀⠀⠀⠀⠀⠃⠀⠀⠀⠘⠙⢃⣾⣿⠃⠀⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣿⣿⡇⢠⡾⢻⡿⠿⢷⣦⣤⠁⣷⣄⣤⣾⠿⠿⢿⣿⣄⠀⣯⣀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠃⠈⠡⠾⣿⣿⣿⡿⠁⠀⣼⣿⣿⡿⠛⢶⣿⣿⣿⠀⠹⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡇⠀⠀⠀⠀⠈⡹⠏⠀⠀⢻⣿⣿⣷⠀⠀⠙⠻⣿⡇⣠⡼⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠀⠀⠀⠀⠈⠀⠀⠀⠀⣸⣿⣿⣿⣧⠀⠀⠀⣿⠀⢿⡻⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠀⠀⣼⣿⠀⠀⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀BETTER CALL SAUL HEISENBERG
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡿⡄⠀⠀⠀⠀⠀⠀⠉⢳⣶⣿⣿⣿⣯⡀⢸⣧⣼⡀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⢀⠀⠀⠀⡀⠀⠀⠀⢸⡅⢘⣟⣽⣿⣿⣿⣿⣿⠤⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣮⡀⡀⠀⠙⠛⠛⠛⠛⠿⠻⣿⣿⣿⣿⣻⣧⡿⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⠀⠀⠀⠀⠀⠐⠛⠃⠀⠛⣿⣿⣿⣿⣿⣷⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣬⣿⣿⣷⣴⣦⠀⠀⠀⠀⣀⡀⣴⣿⣿⣿⣿⣿⣿⢸⣟⢢⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⠻⣿⡷⢷⣦⠴⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⠀⢲⣾⡿⠦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠛⢦⣀⠀⠐⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣷⣶⣾⣯⣄⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠉⠳⣦⣀⣀⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⣨⡿⢟⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢀⣼⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣴⣿⣿⢿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
'''
