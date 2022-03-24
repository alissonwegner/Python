valor = int(input("digite um valor total da conta de luz: "))
kwh = int(input("digite um valor total de :KWh "))
relogio = int(input("digite um valor do relogio: "))
relogio = (relogio * 100)

pt = relogio/kwh
valor_final = valor/pt
resto = 100-pt

print(f'o valor da porcentagem é ', pt, '%')
print(f'o valor que tu deve pagar é ', valor_final)
print(f'o valor que o seu alfredo deve pagar é ', resto)
