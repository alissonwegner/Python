#7.Faça um Programa que leia três números e mostre o maior e o menor deles.
valor = int(input("valor?\n"))
valor2 = int(input("valor2?\n"))
valor3 = int(input("valor3?\n"))
if valor > valor2 and valor > valor3 :
    print(f" valor {valor} é maior ")
elif valor2 > valor and valor2 > valor3 :
    print(f" valor {valor2} é maior ")
else :
    print(f" valor {valor3} é maior ")
