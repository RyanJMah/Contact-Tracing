import mysql.connector
import pandas as pd

#sudo apt-get install mysql-client-core-8.0
#sudo pip3 install mysql-connector-python
#sudo pip3 install pandas

def add_user(uuid, has_covid):
    
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )

    cursor = db.cursor()
    sql = "INSERT INTO users(uuid, has_covid) VALUES (%s, %s)"
    val = (uuid, has_covid)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    db.close()
    return 

def read_user():

    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )
    df = pd.read_sql("SELECT * FROM users", db)

    db.close()
    return df

def add_incident(uuid1, uuid2, distance, longitude, latitude, date_and_time):

    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )

    cursor = db.cursor()
    sql = "INSERT INTO incidents(uuid1, uuid2, distance, longitude, latitude, date_and_time) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (uuid1, uuid2, distance, longitude, latitude, date_and_time)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    db.close()
    return

def read_incident():
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )
    df = pd.read_sql("SELECT * FROM incidents", db)

    db.close()
    return df

def Update_user_covid_status(uuid,covid_status):
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )

    cursor = db.cursor()
    cursor.execute(f'''
                UPDATE db.users
                SET has_covid = {covid_status}
                WHERE uuid = '{uuid}\''''
                )
    db.commit()




if __name__ == "__main__":
    
