import speedtest
on = speedtest.Speedtest()
velocidade = on.download()
print('valor download: {}' .format(round(velocidade)))
