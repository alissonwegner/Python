#9.Faça um Programa que leia três números e mostre-os em ordem decrescente.
p1 = input("Digite o 1° preço: ")
p2 = input("Digite o 2° preço: ")
p3 = input("Digite o 3° preço: ")
if p1 < p2 and p1 < p3 :
    menor = p1    
elif p2 < p1 and p2 < p3:
    menor = p2    
elif p3 < p1 and p3 < p2:
    menor = p3  
if p1 > p2 and p1 > p3:
    maior = p1    
elif p2 > p1 and p2 > p3:
    maior = p2    
elif p3 > p1 and p3 > p2:
    maior = p3  
if p1 > menor and p1 < maior:
    metade = p1
elif p2 > menor and p2 < maior:
    metade = p2
elif p3 > menor and p3 < maior:
    metade = p3
print(f"o maior numero e {maior} ")
print(f"seguido de {metade}")
print(f"e menor e {menor}")