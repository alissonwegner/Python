#14.Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:

#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se 
# o conceito for D ou E.
p1 = float(input("Digite um numero \n"))
p2 = float(input("Digite um numero \n"))
media = float((p1 +p2)/2)
print(f"{media}")
if media >9 and media <= 10 :
    conceito = "a"
elif media >= 7.5 and media < 9 :
    conceito = "b"
elif media >= 6 and media < 7.5 :
    conceito = "c" 
elif media >= 4 and media < 6 :
    conceito = "d"    
elif media >= 0 and media < 4 :
    conceito = "e"

if conceito == "a" or conceito == "b" or conceito == "c":
    print("aprovado")
elif conceito == "d" or conceito == "e" :
    print("reprovado")