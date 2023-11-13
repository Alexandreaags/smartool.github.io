from sqlalchemy import create_engine

import pymysql

import pandas as pd

sqlEngine       = create_engine('mysql+pymysql://ipk:fraunhoferipk@192.168.137.1', pool_recycle=3600)

dbConnection    = sqlEngine.connect()

frame           = pd.read_sql("select ID, data_2 from arduino.sql_data WHERE ID > 500 ", dbConnection)

#pd.set_option('display.expand_frame_repr', False)

print(frame) 

dbConnection.close()