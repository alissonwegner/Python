#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
mb=int(input("informe o tamanho do arquivo"))
velocidade = int(input("informe a velocidade"))
tempo= mb/velocidade
tempo = tempo /60
print(f"falta {tempo} min para termina download")
#print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60))
