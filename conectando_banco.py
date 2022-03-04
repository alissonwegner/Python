import mysql.connector
con = mysql.connector.connect(host='172.16.138.92',
                                database='lilcake',
                                user='remoto',
                                password='remoto')

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao servidor", db_info)
    cursor = con.cursor()
    cursor.execute("describe log;")
  #  linha= cursor.fetchone()

for x in cursor:
  print(x)
#cursor.close()
con.close()


