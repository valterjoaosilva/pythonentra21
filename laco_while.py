n1 = 1

while(n1 <= 10):
    if(n1 % 2 == 0):
        print(n1)
    n1 = n1 + 1
    
n2 = 1

while(n2 <= 10):
    if(n2 % 2 != 0):
        print(n2)
    n2 = n2 + 1
    
valor = int(input('informe o valor da tabuada: '))
for x in range(1,11):
    print(str(x) + '  x ' + str(valor) + ' = '+ str(x * valor))
    
