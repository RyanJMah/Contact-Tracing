import mysql.connector
import pandas as pd

#sudo apt-get install mysql-client-core-8.0
#sudo pip3 install mysql-connector-python
#sudo pip3 install pandas

def add_user(uuid, username, password):

    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "",
        database = "db"
    )

    cursor = db.cursor()
    sql = "INSERT INTO users(uuid, username, password) VALUES (%s, %s, %s)"
    val = (uuid, username, password)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    db.close()
    return

def read_user():

    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "",
        database = "db"
    )
    df = pd.read_sql("SELECT * FROM users", db)

    db.close()
    return df

def add_incident(uuid1, uuid2, distance, longitude, latitude, date_and_time):

    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "",
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
        password = "",
        database = "db"
    )
    df = pd.read_sql("SELECT * FROM incidents", db)

    db.close()
    return df
