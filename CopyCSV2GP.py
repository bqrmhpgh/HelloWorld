import os
import psycopg2
from psycopg2.extras import RealDictCursor, execute_values
import pandas as pd

DB_NAME = 'gp_sydb'
USER_NAME = 'gpadmin'
PASS = 'sk.2019'
HOST_NAME = '10.168.1.20'
PORT = '5432'
#Data_Dir = os.getcwd() + '/export'
Base_Dir = r"E:\01 WorkFiles\csv export\h5"
Data_Dir = Base_Dir+ r"\Tables"
Temp_Dir = Base_Dir

for parent, dirnames, filenames in os.walk(Data_Dir, followlinks=True):
    print(parent)
    for filename in filenames:
        file_path = os.path.join(parent, filename)
        name, extension = os.path.splitext(filename)
        if extension != '.csv':
            continue
        print(name)
        name = "omc." + name.lower()
        '''
        try:
            df = pd.read_csv(file_path)
        except:
            continue

        print(df.shape)
        if df.shape[0] == 0:
            continue

        fff = parent.split("Tables\\", 1)
        tablename = fff[1].replace("\\","_")+"_"+name

        df.insert(0,'logdate',"'2019-01-14'")
        df.insert(0, 'StreamId', 4600000000)
        csv_file = os.path.join(Temp_Dir, name+"_conv") + '.csv'
        df.to_csv(csv_file, index=False, header=False,encoding='utf-8')
        '''
        with open(file_path, 'r', encoding='utf-8') as f:
            #f.readline();
            with psycopg2.connect(database=DB_NAME, user=USER_NAME, password=PASS, host=HOST_NAME, port=PORT,
                                  client_encoding="utf-8") as conn:
                with conn.cursor() as cur:
                    try:
                  #      cur.copy_from(f, name, sep=',')
                  #      os.rename(file_path, os.path.join(file_path, ".done"))
                        cur.copy_expert("COPY " + name + " FROM STDIN WITH CSV HEADER DELIMITER AS ','", f)
                    except psycopg2.DataError as e:
                        print('DataError except:', e)
                        print("Error copying {0}.".format(name))
                        continue
                    except psycopg2.OperationalError as e:
                        print('OperationalError except:', e)
                        print("Error copying {0}.".format(name))
                        continue
                    except psycopg2.ProgrammingError as e:
                        print('ProgrammingError except:', e)
                        print("Error copying {0}.".format(name))
                        continue
                    pass
                pass




