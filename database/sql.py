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

<<<<<<< HEAD
def update(table_name, column, new_value, id):
=======
def lookup_user(uuid):
>>>>>>> 87556c67bc7b522e238e00bf972615f971821671
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )
<<<<<<< HEAD
    cursor = db.cursor()
    sql = f"UPDATE {table_name} SET {column} = %s WHERE id = %s"
    val = (new_value, id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    db.close()
    return

if __name__ == "__main__":
    add_user("nsadad", 1)
    print(read_user())
    update("users",'has_covid', 60, 4)
    print(read_user())
=======
    df = pd.read_sql(f"SELECT * FROM user WHERE uuid = {uuid}", db)

    db.close()
    return df

def lookup_incident(uuid1, uuid2, distance):
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )
    
    df = pd.read_sql(f"SELECT * FROM user WHERE uuid1 = {uuid1} AND uuid2 = {uuid2} AND distance = {distance}")
    db.close()

    return df

>>>>>>> 87556c67bc7b522e238e00bf972615f971821671
