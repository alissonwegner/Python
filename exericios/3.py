#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
valor = input("valor?\n")
if valor == "f" or valor == "F":
    print(f"mulher")
elif valor == "m" or valor == "M":
    print(f"Homem")
else:
    print(f"sexo invalido")