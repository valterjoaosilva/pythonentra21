n1 = float(input("informe um valor inteiro: "))
n2 = float(input("informe um valor inteiro: "))
print("resultado da adição: n1 + n2 = " + str(n1 + n2) )
print("resultado da subtração: n1 - n2 = " + str(n1 - n2) )
print("resultado da multiplicação: n1 x n2 = " + str(n1 * n2) )
#controlando casas decimais
#passo percentual ponto número de casas que desejo flutuar
#como vou definir através do simbolo percentual quais variáveis vão receber a variação de ponto flutuante não precisa concatenar e nem mesmo converter
print("resultado da adição: n1 / n2 = %.2f" % (n1 / n2) )

#convertendo em mais de duas casas decimais e trabalhando com ponto flutuante
print("resultado da adição primeiro valor %.3f, segundo valor %.5f: " % (n1,  n2))
print("resultado da adição: n1 + n2 = %.2f: " % (n1 + n2) )