import mysql.connector
import pandas as pd

def add_user(mac_adr, has_covid):

    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )

    cursor = db.cursor()
    sql = "INSERT INTO users(mac_adr, has_covid) VALUES (%s, %s)"
    val = (mac_adr, has_covid)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    db.close()
    return

def read_user(mac_adr = '', has_covid = None):
    #call like:
    #read_user(mac_adr = '', has_covid = '')
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )
    if(mac_adr == '' and has_covid == None):
        df = pd.read_sql("SELECT * FROM users", db)
    elif(mac_adr != '' and has_covid == None):
        df = pd.read_sql(f"SELECT * FROM users WHERE mac_adr = '{mac_adr}'", db)
    elif(mac_adr == '' and has_covid != None):
        df = pd.read_sql(f"SELECT * FROM users WHERE has_covid = {has_covid}", db)
    elif(mac_adr != '' and has_covid != None):
        df = pd.read_sql(f"SELECT * FROM users WHERE has_covid = {has_covid} AND mac_adr = '{mac_adr}'", db)

    db.close()
    return df

def add_incident(mac_adr1, mac_adr2, rssi, longitude, latitude, date_and_time):

    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )

    cursor = db.cursor()
    sql = "INSERT INTO incidents(mac_adr1, mac_adr2, rssi, longitude, latitude, date_and_time) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (mac_adr1, mac_adr2, rssi, longitude, latitude, date_and_time)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    db.close()
    return

def read_incident(mac_adr1 = '', mac_adr2 = '', rssi = ''):
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )
    #call like:
    #read_incident(mac_adr1 = '', mac_adr1 = '', rssi = '')
    if (mac_adr1 == '' and mac_adr2 == '' and rssi == ''):
        df = pd.read_sql("SELECT * FROM incidents", db)
    elif(mac_adr1 == '' and mac_adr2 == '' and rssi != ''):
        df = pd.read_sql(f"SELECT * FROM incidents WHERE rssi >= {rssi}", db)
    elif(mac_adr1 != '' and mac_adr2 != '' and rssi == ''):
        df = pd.read_sql(f"SELECT * FROM incidents WHERE mac_adr1 = '{mac_adr1}' AND mac_adr2 = '{mac_adr2}'", db)
    elif(mac_adr1 != '' and mac_adr2 == '' and rssi == ''):
        df = pd.read_sql(f"SELECT * FROM incidents WHERE mac_adr1 = '{mac_adr1}'", db)
    elif(mac_adr1 == '' and mac_adr2 != '' and rssi == ''):
        df = pd.read_sql(f"SELECT * FROM incidents WHERE mac_adr2 = '{mac_adr2}'", db)

    db.close()
    return df


def Update_user_covid_status(mac_adr,covid_status):
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
                WHERE mac_adr = '{mac_adr}\''''
                )
    db.commit()
    db.close()
    return

def Update_mac_adr(mac_adr,new_mac_adr):
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )

    cursor = db.cursor()
    cursor.execute(f'''
                UPDATE db.users
                SET mac_adr = '{new_mac_adr}'
                WHERE mac_adr = '{mac_adr}\''''
                )
    db.commit()

    db.close()
    return

def close_contacts(mac_adr):
    list_of_incidents = read_incident(rssi = '-76').values # Update rssi to 6ft value
    list_of_users  = read_user().values
    close_contact = "Safe"

    for i in list_of_incidents:
        if mac_adr == i[1]:
            for j in list_of_users:
                if i[2] == j[1] and int(j[2]) == 1 :
                    close_contact = "Close Contact"
                    break

        elif mac_adr == i[2]:
            for j in list_of_users:
                if i[1] == j[2] and int(j[2]) == 1 :
                    close_contact = "Close Contact"
                    break

        if close_contact == "Close Contact":
           break
    return(close_contact)   
