import json
import requests

def location():

	response = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey=aaaf819d25a84c3c84f09ac62f39c8d8")

	res = response.json()
	data = {}

	data["latitude"] = res["latitude"]
	data["longitude"] = res["longitude"]
	data["time"] = res["time_zone"]["current_time"]

	return data

def lookup_user(uuid):
    db = mysql.connector.connect(
        host = "34.67.23.158",
        user = "root",
        password = "password123",
        database = "db"
    )
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
    
    df = pd.read_sql(f"SELECT * FROM incident WHERE uuid1 = {uuid1} AND uuid2 = {uuid2} AND distance = {distance}")
    db.close()

    return df