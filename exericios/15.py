#15.Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, 
# caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
p1 = int(input("Digite um numero \n"))
p2 = int(input("Digite um numero \n"))
p3 = int(input("Digite um numero \n"))
if p1 + p2 > p3:
    if p1 == p2 and p1 == p3:
        print 'Triângulo Equilátero'
    elif p1 == p2 or p2 == p3 or p1 == p3:
        print 'Triângulo Isósceles'
    elif p1 != p2 and p3 or p2 != p1 and p3 or p1 != p3:
        print 'Triângulo Escaleno'
else:
    print 'É impossivel ser um triângulo'