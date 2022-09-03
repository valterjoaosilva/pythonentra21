produto = ['bala','laranja', 'camisa', 'calça', 'short']
print(len(produto))
print(produto)

item = input('Informe o item a ser excluido? ')
existe = False

for x in range(0,len(produto)):
    if(item == produto[x]):
        produto.remove(item)
        existe = True
        break

print(produto)
if(existe):
    print('O item ' + item + ' foi removido')        
else:
    print('O item '+ item +' não existe na lista')
    
print(produto)