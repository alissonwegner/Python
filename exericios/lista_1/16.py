#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = int(input("quantos metros vao ser pintado ?"))
quant_litros = metros/3
quant_litros= int(quant_litros)
if metros % 3 != 0 :
    quant_litros += 1
quant_latas = quant_litros / 18
quant_latas= int(quant_latas)
if quant_litros % 18 != 0 :
    quant_latas += 1
valor_total = quant_latas * 80
print( "e necessario", quant_latas, " para ser feito a pintura")
print("foi gasto R$:" ,valor_total)