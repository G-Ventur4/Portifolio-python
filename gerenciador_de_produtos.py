import csv
import datetime
import sys


def cadastrar_produto():
    produto = {}
    produto['nome'] = input('Digite o nome do produto: ')
    produto['descricao'] = input('Digite a descrição do produto: ')
    produto['preco'] = float(input('Digite o preço do produto: '))
    produto['estoque'] = int(input('Digite o estoque do produto: '))
    produto['data_registro'] = datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')

    return produto

def remover_produto(produtos):
    nome_produto = input('Digite o nome do produto que deseja remover: ')
    for produto in produtos:
        if produto['nome'] == nome_produto:
            produtos.remove(produto)
            print('Produto removido com sucesso')
            break
    else:
        print('Produto não encontrado')

def procurar_produto(produtos):
    nome_produto = input('Digite o nome do produto que deseja procurar: ')
    for produto in produtos:
        if produto['nome'] == nome_produto:
            print(produto)
            break
    else:
        print('Produto não encontrado')

def ver_produtos(produtos):
    for produto in produtos:
        print(produto)

def salvar_csv(produtos):
    with open('estoque.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['nome', 'descricao', 'preco', 'estoque', 'data_registro'])
        for produto in produtos:
            writer.writerow([produto['nome'], produto['descricao'], produto['preco'], produto['estoque'], produto['data_registro']])
    print('Estoque salvo com sucesso.')
    sys.exit()

def main():
    produtos = []

    print('Bem-vindo ao sistema de gerenciamento de Estoque')

    while True:
        print('\nMenu:')
        print('1 - Cadastrar produto')
        print('2 - Remover produto')
        print('3 - Procurar produto')
        print('4 - Ver produtos')
        print('5 - Salvar em .csv e Sair')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            produtos.append(cadastrar_produto())
        elif opcao == 2:
            remover_produto(produtos)
        elif opcao == 3:
            procurar_produto(produtos)
        elif opcao == 4:
            ver_produtos(produtos)
        elif opcao == 5:
            salvar_csv(produtos)

if __name__ == '__main__':
    main()