fruta = ('maca', 'laranja', 'pera', 'amora')

desejo = input('Qual fruta você quer?')
for x in range(0,len(fruta)):
    if(desejo == fruta[x]):
        print (desejo + " estana na posição: " + str(x))