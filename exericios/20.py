#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
p1 = int(input("Digite um numero \n"))
p2 = int(input("Digite um numero \n"))
p3 = int(input("Digite um numero \n"))
media = (p1+p2+p3)/3
if media >= 7 :
    if media >= 10:
        print('Aprovado com Distinção')
    else :
        print("Aprovado")
else :
    print("Reprovado")