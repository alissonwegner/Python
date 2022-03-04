import mysql.connector
from datetime import datetime
import random
now = datetime.now()
hora=now.hour
if (hora > 8 and hora < 23 ):

    print ("hora",hora)
    temp=int(random.randrange(1, 20))
    print(temp)