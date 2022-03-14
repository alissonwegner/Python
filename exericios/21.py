#Faça um Programa para um caixa eletrônico. O programa deverá perguntar 
# ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar 
# com a quantidade de notas existentes na máquina.
valor = int(input("Digite o valor \n"))
if valor <10 or valor > 600 :
    print("valor nao pode ser sacado")
else :
    nota_100 = int(valor /100)
    valor = int(valor % 100)
    nota_50 = int(valor /50)
    valor = int(valor % 50)
    nota_10 = int(valor /10)
    valor = int(valor % 10)
    nota_5 = int(valor /5)
    valor = int(valor % 5)
    nota_1 = int(valor)
print("vai sacar \n", nota_100, "notas de R$100, \n", nota_50, "notas de R$50, \n", nota_10, "notas de R$10, \n", nota_5, "notas de R$5 \n", nota_1, "notas de R$1")