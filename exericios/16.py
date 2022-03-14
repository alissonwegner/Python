#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
a = float(input("Digite um numero \n"))
b = float(input("Digite um numero \n"))
c = float(input("Digite um numero \n"))
if a == 0 :
    print(" a esqueção não é do segundo grau!")
x=(b**2)-(4*a*c)
if x<0 :
        print ("Raiz negativa nao pode ser extraida.")
else :
    x=math.sqrt(x)
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
print "\n\nX' = %s \nX'' = " % x1, x2
