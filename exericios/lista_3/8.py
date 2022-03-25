#8.Faça um programa que leia 5 números e informe a soma e a média dos números.
soma=0
for i in range(0, 5):
    numero = int(input('Informe um numero: '))
    soma += numero

soma = soma/5
print("media dos numero é de :", soma)
