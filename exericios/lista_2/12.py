#12.Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do 
# salário bruto (conforme tabela abaixo)
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a 
# quantidade de horas trabalhadas no mês.
#        Desconto do IR:
#        Salário Bruto até 900 (inclusive) - isento
#        Salário Bruto até 1500 (inclusive) - desconto de 5%
#        Salário Bruto até 2500 (inclusive) - desconto de 10%
#        Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
valor_hora = float(input("qual o valor da hora?\n"))
hora_trabalhada = float(input("quantas horas por dia voce trabalha ?\n"))
hora_trabalhada = hora_trabalhada * 22
salario_bruto = valor_hora * hora_trabalhada
print(f"o seu salario bruto é de {salario_bruto}")
if salario_bruto <= 900 :
    print(f"voce é isento")
elif salario_bruto <= 1500 and salario_bruto > 900:
    salario_liquido = salario_bruto - (salario_bruto * 0.05)
    print(f"desconto de 5% ficando {salario_liquido}")
elif salario_bruto <= 2500 and salario_bruto > 1500:
    salario_liquido = salario_bruto - (salario_bruto * 0.10)
    print(f"desconto de 10% ficando {salario_liquido}")    
elif salario_bruto > 2500:
    salario_liquido = salario_bruto - (salario_bruto * 0.20)
    print(f"desconto de 20% ficando {salario_liquido}")   