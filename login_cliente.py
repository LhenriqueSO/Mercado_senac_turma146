#Login Cliente
print("  Login Cliente   ")
print("                  ")
print("(1) Fazer Login   ")
print("(2) Fazer Cadastro")
print("                  ")                 

direcionar= int(input("Opção Menu: "))

match direcionar:
    case 1:
        email=input("Informe O Email: ")
        senha= input("Informe a Senha: ")
    case 2:
        ''' nome=
            data nascimento=
            endereço=
            cpf=
            sexo=
            
        '''
        print("cadastro")
    case _:
        print("Informe uma opção válida!")


