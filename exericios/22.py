#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
valor = int(input("Digite o valor \n"))
if valor % 2 == 0 :
    print("par")
else :
    print("impar")