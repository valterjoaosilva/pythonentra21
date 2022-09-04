#dicionarios

dicionario = {1, 2, 3}
print(type(dicionario))
numero = {'caioba': 'laranja', 'batario':'ameixa', 'cecliterio': 'goiaba', 'binitario': 'maça' }
print(numero['batario'])
print(len(numero))
print(numero.get('cecliterio'))
print(numero.get(6))

fruta = input('Informe o indice da fruta: ')
if(fruta == None):
    print('Inexistente')
else:
    print('A fruta é: '+ str(numero[fruta]))