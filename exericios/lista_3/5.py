# 5.Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
#pais_A = 80000
#pais_B = 200000


crecimento_a = 1.03
crecimento_b = 1.015
pais_A = int(input('Informe a populacao do pais A: '))
while (pais_A <= 0):
    pais_A = int(input('Informe um valor valido: '))

crecimento_a = float(input('Informe o crescimento do pais A: '))
while (crecimento_a <= 0):
    crecimento_a = float(input('Informe um valor valido: '))

pais_B = int(input('Informe a populacao do pais B: '))
while (pais_B <= 0):
    pais_B = int(input('Informe um valor valido: '))

crecimento_b = float(input('Informe o crecimento do pais B: '))
while (crecimento_b <= 0):
    crecimento_b = float(input('Informe um valor valido: '))




anos=1
while(pais_A <= pais_B):
    pais_A *=  crecimento_a
    pais_B *=  crecimento_b
    anos += 1

print(f'Vai levar {anos} anos para Cidade A ultrapassar a Cidade B')