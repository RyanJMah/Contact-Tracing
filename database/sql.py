import mysql.connector
import pandas as pd

def main():
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "UwU",
        database = "db"
    )
    
    df = pd.read_sql("SELECT * FROM users", db)
    print(df)

if __name__ == "__main__":
    main()