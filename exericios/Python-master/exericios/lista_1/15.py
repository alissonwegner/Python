#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
quat_hora = int(input("quantas horas voce trabalhou ?"))
quat_trabalhada = int(input("quanto voce ganha por hora ?"))
salario_total = quat_hora * quat_trabalhada
print("quantidade salario brutodo mes :", salario_total)
insposto = salario_total * 0.011
salario_total = salario_total - insposto
print("imposto", insposto)
inss = salario_total * 0.008
salario_total = salario_total - inss
print("INSS",inss)
sindicato = salario_total * 0.005
salario_total = salario_total - sindicato
print("sindicato", sindicato)
print("salario liquido : ", salario_total) 

