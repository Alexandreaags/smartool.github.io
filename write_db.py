from sqlalchemy import create_engine
 
import pymysql

from time import sleep

import pandas as pd
 
 
 
userVitals = {"data_1":[120],
              "data_2":[120],
              "data_3":[120],
              "data_4":[120],
              "data_5":[120],
              "data_6":[120],
              "data_7":[120],
              "data_8":[120],
              "data_9":[120],
              "data_10":[120],}
 
 
 
tableName   = "sql_data"
 
dataFrame   = pd.DataFrame(data=userVitals)          
 
 
sqlEngine       = create_engine('mysql+pymysql://ipk:fraunhoferipk@192.168.137.1/arduino', pool_recycle=3600)
 
dbConnection    = sqlEngine.connect()

i=0

try:
    while i<100:
        frame           = dataFrame.to_sql(tableName, dbConnection, if_exists='append', chunksize=1000, index= False)
        i+=1
        print(i)
        # sleep(.010)
except ValueError as vx:

    print(vx)

except Exception as ex:  

    print(ex)

else:

    print("Table %s created successfully."%tableName)

finally:
    
    dbConnection.close()