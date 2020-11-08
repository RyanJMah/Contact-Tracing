import mysql.connector
import pandas as pd

def add_user():
    return
def read_user():
    return
def add_incidents():
    return
def read_incidents():
    return

def main():
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "",
        database = "db"
    )
    
    df = pd.read_sql("SELECT * FROM users", db)
    print(df)
if __name__ == "__main__":
    main()