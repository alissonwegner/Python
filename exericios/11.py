#11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#   Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#        o salário antes do reajuste;
#        o percentual de aumento aplicado;
#        o valor do aumento;
#        o novo salário, após o aumento. 
#print("teste")
salario = float(input("qual o salario ?\n"))
if salario <= 280.00:
    novo_salario = salario + (salario * 0.20)
    print(f"o salario antigo é de R$ {salario}, \n com aumento de 20% vai ficar = R$ {novo_salario}")
elif salario <= 700.00 and salario > 280.00:
    novo_salario = salario + (salario * 0.15)
    print(f"o salario antigo é de R$ {salario}, \n com aumento de 15% vai ficar = R$ {novo_salario}")
elif salario <= 1500.00 and salario > 700.00:
    novo_salario = salario + (salario * 0.10)
    print(f"o salario antigo é de R$ {salario}, \n com aumento de 10% vai ficar = R$ {novo_salario}")
elif salario > 1500.00:
    novo_salario = salario + (salario * 0.05)
    print(f"o salario antigo é de R$ {salario}, \n com aumento de 5% vai ficar = R$ {novo_salario}")
