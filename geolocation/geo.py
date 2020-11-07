import json
import requests

def location():

	response = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey=aaaf819d25a84c3c84f09ac62f39c8d8")

	res = response.json()
	data = {}

	data["latitude"] = res["latitude"]
	data["longitude"] = res["longitude"]
	data["current_time"] = res["time_zone"]["current_time"]

	return data



