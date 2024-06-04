from operacoesbd import *

opcao = -1
conexao = criarConexao('endereco', 'usuario', 'senha', 'bancodedados')
print('Bem-vindo ao sistema de manifestações do cliente da Universidade XYZ!\n')

while opcao != 7:
    print('\nEscolha o que deseja fazer:\n'
          ' 1) Listagem das Manifestações\n'
          ' 2) Listagem de Manifestações por Tipo\n'
          ' 3) Criar uma nova Manifestação\n'
          ' 4) Exibir quantidade de manifestações\n'
          ' 5) Pesquisar uma manifestação por código\n'
          ' 6) Excluir uma Manifestação pelo Código\n'
          ' 7) Sair do Sistema\n')
    opcao = int(input("Digite a sua opção: "))

# 1) Listagem das Manifestações
    if opcao == 1:
        consultaListar = 'select * from manifestacoes'
        manifestacoes = listarBancoDados(conexao, consultaListar)

        if len(manifestacoes) == 0:
            print('Não existem manifestações a serem exibidas!')
        else:
            print("Lista de manifestações")
            for item in manifestacoes:
                print('\nCódigo:', item[0], '\nTipo:', item[2], '\nManifestação:', item[1])

# 2) Listagem de Manifestações por Tipo

    elif opcao == 2:
        tipoDeManifestacao = input('Qual tipo de manifestação você gostaria que fosse listada?')
        consultaListarPorTipo = "select * from manifestacoes where tipo = '" + tipoDeManifestacao + "'"
        manifestacoes = listarBancoDados(conexao, consultaListarPorTipo)

        if len(manifestacoes) == 0:
            print("\nNão existem manifestações a serem exibidas para o tipo informado!")
        else:
            print("\nLista de Manifestações do Tipo:", tipoDeManifestacao)
            for item in manifestacoes:
                print('Código', item[0], '- Manifestação', item[1], '- Tipo', item[2])

# 3) Criar uma nova Manifestação

    elif opcao == 3:
        manifestacaoTipo = ""
        manifestacaoNova = ""

        manifestacaoTipo = input("Qual tipo de manifestação você gostaria de adicionar ao sistema?: ")
        manifestacaoNova = input("Por favor insira a manifestação que gostaria de adicionar: ")

        if not manifestacaoTipo:
            print('Você não inseriu nada!')

        else:
            consultaInsert = 'insert into manifestacoes (Tipo,Manifestacao) values(%s,%s)'
            dados = [manifestacaoTipo, manifestacaoNova,]

            insertNoBancoDados(conexao, consultaInsert, dados)
            print("\nManifestação adicionada com sucesso!")

# 4) Exibir quantidade de manifestações

    elif opcao == 4:
        consultaQuantidade = "select * from manifestacoes where codigo > 0 "
        manifestacoes = listarBancoDados(conexao, consultaQuantidade)
        print("\nTemos", len(manifestacoes), "Manifestações cadastradas no sistema")

# 5) Pesquisar uma manifestação por código

    elif opcao == 5:
        codigoPesquisa = input('Por favor insira o código da manifestação que você gostaria de ver: ')
        consultaCodigo = "select * from manifestacoes where codigo = '" + codigoPesquisa + "'"
        codigoPesquisaResultado = listarBancoDados(conexao, consultaCodigo)
        print('A manifestação requisitada foi:', codigoPesquisaResultado)

# 6) Excluir uma Manifestação pelo Código

    elif opcao == 6:
        codigoApagar = input('\nPor favor insira o código da manifestação que você quer apagar: ')

        consultaCodigo = "delete from manifestacoes where codigo = %s"

        codigoApagarLista = [codigoApagar]

        excluir = excluirBancoDados(conexao, consultaCodigo, codigoApagarLista)

        if excluir == 0:
            print('\nManifestação não encontrada no sistema (Não existe/Já foi removida)')
        else:
            print('\nManifestação excluída com sucesso')

encerrarBancoDados(conexao)
print('👋 Tchau tchau! 👋')
