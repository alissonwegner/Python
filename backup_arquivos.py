import os
from datetime import date
data_atual = date.today()
print(data_atual)
pasta = "/home/alisson/Downloads"

os.system('cd /home/alisson/Documentos/bk && mkdir %s' %(data_atual))
bk = ('/home/alisson/Documentos/bk/%s' %(data_atual))
#os.system('mv %s %s'%(pasta, bk))

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        #print(os.path.join(arquivo))
        os.system('mv %s %s'%(arquivo, bk))