
import json


import urllib.request
contents = urllib.request.urlopen("https://api.ipgeolocation.io/ipgeo?apiKey=aaaf819d25a84c3c84f09ac62f39c8d8").read()

print(contents)

print("fuck this")
