lista=[]

def adicionar_inicio(lista):
    item=''
    while item.lower()!='s':
        item=input("Insira o elemento ou digite 's' para finalizar: ")
        if item!='s':
            lista.insert(0,item)
            print(lista)

def adicionar_fim(lista):
    item=''
    while item.lower()!='s':
        item=input("Insira o elemento ou digite 's' para finalizar: ")
        if item!='s':
            lista.append(item)
            print(lista)
    
def remover_elemento():
    item=input('Digite o item a ser removido: ')
    for value in lista:
        if value==item:
            lista.remove(item)
            return f'O elemento {item} foi removido.'
    return 'Este elemento não pertence a lista.'
        
def tamanho_lista(lista):
    return len(lista)

def imprimir_lista(lista):
    for item in lista:
        print(item)
        
def esvaziar_lista(lista):
    lista.clear()
    
def opcao():
    print('1 - Inserir elemento no início da lista')
    print('2 - Inserir elemento no final da lista')
    print('3 - Remover elemento da lista')
    print('4 - Retornar o tamanho da lista')
    print('5 - Imprimir a lista')
    print('6 - Esvaziar a lista')
    print('7 - Sair do programa')

def menu():
    escolha=0

    while escolha!=7:
        opcao()
        escolha=int(input('>> '))
        if escolha==1:
            adicionar_inicio(lista)
            
        elif escolha==2:
            adicionar_fim(lista)
            
        elif escolha==3:
            print(remover_elemento())
            
        elif escolha==4:
            print(f'Tamanho da lista: {tamanho_lista(lista)}')
            
        elif escolha==5:
            imprimir_lista(lista)
            
        elif escolha==6:
            esvaziar_lista(lista)
            print('A lista foi esvaziada.')
            print(f'Lista: {lista}')
            
        elif escolha==7:
            print('Saindo do programa')
            break
            
        else:
            print('Opção inválida.')
        
if __name__=="__main__":
    menu()
