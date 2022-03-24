#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
valor = float(input("informe a altura : "))
valor_2 = input("homem ou mulher ? ")
if (valor_2 == "m") :
    print("o seu peso ideal é : ", ((72.7 * valor)-58))

if (valor_2 == "f") :
    print("o seu peso ideal é : ", ((62.1 * valor)-44.7))
