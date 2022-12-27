import os
import json
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import sqlalchemy as sa
import mysql.connector as sql
import shutil

main_path = '/mnt/c/diary ngoding/Test Telkom/pipeline mongo to mysql/JsonOutput/'
filename = 'vaksin.json'
path_json = os.path.join(main_path, filename)

def json_tolist(path_json):
    json_list = []

    my_file = open(path_json)
    data = my_file.read()
    data_into_list = data.split("\n")
    for x in data_into_list:
        try:
            json_object = json.loads(x)
            json_list.append(json_object)
        except:
            pass
    my_file.close()
    return json_list

def connection_mysql(user,db_name,password,host,port,df,tableName,path_json,filename):
    connection_uri = '{engine}://{user}:{password}@{host}:{port}/{dbname}'.format(engine='mysql+mysqlconnector', user=user, password=password, host=host, port=port, dbname=db_name)
    print(connection_uri)
    engine = create_engine(connection_uri)
    try:
        frame = df.to_sql(tableName, con=engine, if_exists='append', index=False)
    except ValueError as vx:
        print(vx)
        shutil.move(path_json, os.path.join('/mnt/c/diary ngoding/Test Telkom/pipeline mongo to mysql/failed/',filename))
        print("check data in failed folder")
    except Exception as ex:
        print(ex)
        shutil.move(path_json, os.path.join('/mnt/c/diary ngoding/Test Telkom/pipeline mongo to mysql/failed/',filename))
        print("check data in failed folder")
    else:
        print("Table %s created successfully."%tableName);
        os.remove(path_json)

dd = json_tolist(path_json)
df = pd.json_normalize(dd)


#cleansing data
df['createdAt'] = pd.to_datetime(df['createdAt.$date'])
df['updatedAt'] = pd.to_datetime(df['updatedAt.$date'])
df['vaccinePatient.bornDate'] = pd.to_datetime(df['vaccinePatient.bornDate'])
df['vaccination.vaccineDate'] = pd.to_datetime(df['vaccination.vaccineDate'])
df['vaccination.vaccineStatus'] = df['vaccination.vaccineStatus'].astype(int)
df = df.drop ('createdAt.$date', axis=1)
df = df.drop ('updatedAt.$date', axis=1)
print(df.info())


connection_mysql('root',
                'test',
                'password',
                'localhost',
                '3306',
                df,
                'vaksin',
                path_json,
                filename)