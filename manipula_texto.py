#manipulando arquivo texto

texto =list()
arq = open('nossoTexto.txt', 'a')
texto.append('conteudo primeira linha')
texto.append('\ntexto segunda linha')
texto.append('\nconteudo da terceira linha')
arq.writelines(texto)
arq.close()