from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import mysql.connector
def conect():
    con = mysql.connector.connect(host='172.16.138.92',
                                    database='lilcake',
                                    user='remoto',
                                    password='remoto')
    return con

def temp():
    option = Options()
    option.headless = True
    navegador = webdriver.Chrome(options=option)
    navegador.get("https://www.google.com/search?q=temperatura+santa+maria&oq=temperatura+santa+maria&aqs=chrome.0.69i59j0i512l9.4384j1j4&sourceid=chrome&ie=UTF-8")
    titulo=navegador.find_element_by_xpath('//*[@id="wob_tm"]').text
    navegador.quit()
    return titulo


titulo=temp()
print(titulo,"ºC")

#conecta em banco
con=conect()


cursor = con.cursor()
