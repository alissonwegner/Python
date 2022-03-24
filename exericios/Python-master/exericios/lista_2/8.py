#8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
p1 = input("Digite o 1° preço: ")
p2 = input("Digite o 2° preço: ")
p3 = input("Digite o 3° preço: ")

def menor():
    if p1 < p2 and p3 and p1:
        print 'O produto 1 é o mais barato!!'
    elif p2 < p1 and p3:
        print 'O produto 2 é o mais barato!!'
    elif p3 < p1 and p2:
        print 'O produto 3 é o mais barato!!'