# Contact-Tracing
Prototype contact tracing app for hackathon

Names: Yahya Al-Shamali, 
       Roberto Villarreal Andrade, 
       Ryan Mah, 
       Norman Zhang
       
Date: November 7-8, 2020


Running Instructions:
To run this program, 


GUI.py:
Once the program is run, a GUI will pop up

The status indicates whether the user was in close contact with someone who has been tested positive for covid-19.
The status updates every 60 seconds. The user could also update their status instantly by clicking
the Refresh Status button located at the bottom of the GUI.

Your mac address is required so that the program can identify you. The mac address will be stored in a database.
If you update your mac address, it will be updated in the database as well. The user's current mac address is shown
under the input text box.

If the user tests positive, their tester will provide them with a positive test code. Once the code is inputted into the GUI,
the database will update and will notify everyone who was in close contact. This test code is for making sure that all cases reported are guaranteed to be correct for security purporses.


Code Generator.py: 
This program asks for the user's mac address then it will return the positive test code. Only qualified testing professionals are allowed access to this code generator.


Database (sql.py):
Google Cloud SQL database was used to store data of users and incidents. The database is composed of two tables, a users table and an incidents table. 
The users table stores the mac addresses of the users device along with a boolean representing the users covid test results. If there are no test results, the default value is False.
The incidents table stores data on incidents where people are 6-feet or closer. When such an incident occurs, the database will store the mac addresss of both users, the RSSI strength that was reported,
and will utilize a geolocation API to store the latitide, longitiude, and date/time of the incident. The database can add users, add incidents, update the user's covid status, update the mac address, and provide a list of people that an user has been in contact with.


Geolocation (geo.py):
Geolocation API is used to report important information when an incident occurs. This includes the users longitude, latitude and time of incident. When an incident occurs, the program calls upon the geolocation API and the json information is transfered into the database.


BLE Scanner:
