produto = []
def validaAcesso(pUsuario, pSenha):
    while(pUsuario != 'valter' or pSenha != 'proway'):
        print('Login ou senha invalido')
        pUsuario = input('Usuario: ')
        pSenha = input('Senha: ')

def mostraMenu():
    
    
    opcao = 0 
    while(opcao != 5):
        print('+'.ljust(34,'-')+'+')
        print('| 1 - Cadastrar  2 - Alterar    |')
        print('| 3 - Excluir    4 - Visualisar |')
        print('|           5 - Sair            |')   
        print('+'.ljust(34,'-')+'+')
        opcao = int(input('Digite a opção desejada: '))
    
        if(opcao == 1):
            nome = input('Digite o produto: ')
            if(nome in produto):
                print(nome +' produto já cadastrado')
            else:
                produto.append(nome)
                print(nome +' produto cadastrado com sucesso')
        
        elif(opcao == 2):
            nome = input('Digite o produto que deseja substituir: ')
            if(nome in produto):
                for x in range(0,len(produto)):
                    if(produto[x] == nome):
                        novoNomeProduto = input('Digite o novo produto para substituir: '+ nome)
                        produto[x] = novoNomeProduto
                        print(novoNomeProduto+' adicionado com sucesso')
                        break
            else:
                print(nome +' Não cadastrado')
                
        elif(opcao == 3):
            nome = input('Digite o produto que deseja excluir: ')
            if(nome in produto):
                produto.remove(nome)
                print(nome+' foi removido')
            else:
                print(nome+' Não está cadastrado')
        
        elif(opcao == 4):
            if(len(produto) == 0):
                print('não existe produtos cadastrados')
            else:
                print(produto)
        
        elif(opcao == 5):
            print('Obrigado por usar o sistema')
        
        else:
            print('Opção não existe')
            
                    
                