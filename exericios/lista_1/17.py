#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
metros = int(input("quantos metros vao ser pintado ?"))
quant_litros = metros/6
quant_litros= int(quant_litros)
print(f'escolha uma das 3 opçoes \n 1 para somente 18litros \n 2 para galoes de 3,6 litros \n 3 para galoes mistos')
opcao = int(input())
quant_litros= int(quant_litros)
if metros % 6 != 0 :
    quant_litros += 1
if(opcao == 1):
    quant_latas = quant_litros / 18
    if(quant_latas<1):
        quant_latas = 1
    if (quant_litros % 18) != 0 :
        quant_latas += 1
    valor_total = quant_latas * 80
    print("foi gasto R$:" ,valor_total)
if(opcao == 2):
    quant_latas = quant_litros / 3.6
    if(quant_latas<1):
        quant_latas = 1
    if (quant_litros % 3.6) != 0 :
        quant_latas += 1
    valor_total = quant_latas * 25
    print("foi gasto R$:" ,valor_total)
if(opcao == 3):
    quant_latas18 = quant_litros / 18
    if(quant_latas18 <1):
        quant_latas18 = 1
        
    if (quant_litros % 18) != 0 :
        resto18 = quant_litros % 18
        quant_latas3 = resto18 / 3.6
        if(quant_litros % 3.6) != 0 :
            quant_latas3 += 1
        quant_latas3 = int(quant_latas3)
    valor = (quant_latas18 *80)+ (quant_latas3* 25)
    print("foi gasto R$:" ,valor)
    print(f'foi utilizado {quant_latas18} de latas de 18 Litros e {quant_latas3} de latas de 3,6 Litros')