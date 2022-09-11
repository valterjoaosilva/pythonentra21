import matplotlib.pyplot as grafico 

notas = [8, 9, 10, 7]
bimestre = ['primeiro', 'segundo', 'terceiro', 'quarto']

grafico.title('notas bimetrais' )
grafico.plot(bimestre, notas)

grafico.show()
