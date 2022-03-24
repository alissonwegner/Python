#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual 
# operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma 
# frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
p1 = int(input("Digite um numero \n"))
p2 = int(input("Digite um numero \n"))
operacao = input("Digite a operacao \n")
if operacao == "-":
    resultado = p1 - p2
elif operacao == "+":
    resultado = p1 + p2
elif operacao == "/":
    resultado = p1 / p2
elif operacao == "*":
    resultado = p1 * p2
if resultado % 2 == 0:
    par_impar = "par"
else :
    par_impar = "impar"
if resultado == round(resultado):
    int_dec = "Inteiro"
else:
    int_dec = "Decimal"

if resultado > 0 :
    pos_neg = "positiva"
else :
    pos_neg = "negativo"

print(f"\nresultado é",resultado,"\n ", par_impar, "\n",int_dec,"\n",pos_neg)