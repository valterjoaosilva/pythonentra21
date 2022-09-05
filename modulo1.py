def universidade(pUniversidade = 'UFSC'):
    print("A universidade que você estuda:"+pUniversidade)
    
def valida_Acesso(pusuario, psenha):
    if(pusuario == 'VALTER' and psenha == 'PROWAY'):
        print("usuário validado")
    else:
        print("acesso negado")