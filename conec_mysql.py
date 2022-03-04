import mysql.connector
con = mysql.connector.connect(host='127.0.0.1',database='python',user='root',password='root')

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao servidor", db_info)

    con.execute("SHOW TABLES")
    
  

   # cursor.close()
   # con.close()

