
import speedtest  
  
  
st = speedtest.Speedtest()
option = 0
while(option != 3):
    option = int(input('''Escolha uma opção:

    1) Download Speed  
    2) Upload Speed  
    3) Exit
  
    Escolha:
    '''))
    if option == 1:  
        vel_dow=st.download()
        print("Download:", round(vel_dow/1000000,2))
    
    elif option == 2: 
        vel_up=st.upload()
        print(round(vel_up/1000000,2))
