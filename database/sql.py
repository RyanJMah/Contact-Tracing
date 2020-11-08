import mysql.connector
import pandas as pd

def add_user(db, uuid, username, password):
    cursor = db.cursor()
    sql = "INSERT INTO users(uuid, username, password) VALUES (%s, %s, %s)"
    val = (uuid, username, password)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    return 

def read_user(db):
    return pd.read_sql("SELECT * FROM users", db)

def add_incident(db, uuid1, uuid2, distance, longitude, latitude, date_and_time):
    cursor = db.cursor()
    sql = "INSERT INTO incidents(uuid1, uuid2, distance, longitude, latitude, date_and_time) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (uuid1, uuid2, distance, longitude, latitude, date_and_time)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    return

def read_incident(db):
    return pd.read_sql("SELECT * FROM incidents", db)

def main():
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "",
        database = "db"
    )
    
    #add_user(db, "UwU", "Rova", "OwO")
    #add_incident(db, "1", "2", 3, 4, 5, "2020-11-07 05:26:01")
    #read_user(db)
    #read_incident(db)
    
    db.close()

if __name__ == "__main__":
    main()