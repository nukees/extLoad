# -*- coding: utf-8 -*-

# Импортируем внешние библиотеки
import mysql.connector as db
import pandas as pd
import pyexcelerate as xls

if __name__ == "__main__":
    try:
        db_connection = db.connect(host='10.245.41.196', port='3306',user='soctraf', password='traffic', database='traf')
        if db_connection.is_connected():
            print('Connect to BD')
            print('')
    except:
        print('Connection error')

    query = """
    SELECT
    _idhw.A_device AS A_device,
    _idhw.Z_device AS Z_device,
    round(_idhw.peak,1) AS Link_Load
    FROM internal_days _idhw
    WHERE
    _idhw.A_device LIKE '%akta-bngmx%' AND
    _idhw.year = 2019 AND
    _idhw.month = 10 AND
    _idhw.day = 10 AND
    _idhw.traf = 'bps_out'
    """
    df = pd.read_sql_query(query, db_connection)
    print(df)
    
    print('--- Work complete ---')


#