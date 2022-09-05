#funções com parametros

def calcular(px, py):
    print(px/py)
    

x = int(input("passe um valor inteiro: "))
y = int(input("passe um valor inteiro menor que x: "))

if(x > y):
    calcular(x, y)
else:
    print("x é: "+ str(x)+ " que é menor do que y : "+ str(y))














































