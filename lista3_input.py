produto = ['bala','laranja', 'camisa', 'calça', 'short']
print(len(produto))
print(produto)

for x in range(0,len(produto)):
    if('camisa' == produto[x]):
        produto.remove('camisa')
        break
    
print(produto)