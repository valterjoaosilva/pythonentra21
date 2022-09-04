#dicionarios

dicionario = {1, 2, 3}
print(type(dicionario))
numero = {'caioba': 'laranja', 'batario':'ameixa', 'cecliterio': 'goiaba', 'binitario': 'maça' }
print(numero['batario'])
print(len(numero))
print(numero.get('cecliterio'))
print(numero.get(6))

numero['cartago'] = 'melancia'


print(numero)

fruta = input('Informe o indice da fruta que procura: ')
if(fruta == None):
    print('Inexistente')
else:
    print('A fruta é: '+ str(numero[fruta]))

retirar = input('Digite a fruta que quer excluir:')
print(numero.pop(fruta, 'inexistente'))
print(numero)
    

