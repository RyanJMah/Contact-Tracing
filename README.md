# Contact-Tracing
Prototype contact tracing app for hackathon

Names: Yahya Al-Shamali, 
       Roberto Villarreal Andrade, 
       Ryan Mah, 
       Norman Zhang
       
Date: November 7-8, 2020

GUI.py:
Once the program is run, a GUI will pop up

The status indicates weather the user was in close contact with someone who has been tested positive.
The status updates every 60 seconds. The user could also update their status instantly by clicking
the Refresh Status button at the bottom of the GUI.

Your Mac Address is required so that the program can identify you. The mac address will be stored on a database.
If you Update your mac address, it will be updated in the database. The user's current mac address is shown
under the input text box.

If the user gets tested positive, their tester will provide them with a Positive Test Code. Once the code is inputted into the GUI
the database will update and will notify everyone who was a close contact.

Code Generator.py: 
This program asks for the user's mac address then it will return the Positive Test Code

Database:
Cloud SQL google database was used to store data of users and incidents. The database is composed of two tables, a users table and a incidents table. 
The users table stores the Mac Addresses of the users device along with a boolean representing the users covid test results.
The incidents table stores data on incedents where people get 6-feet or closer. This is when the bluethoot signal strength (RSSI) between two different
devices measures to be -75dbm or highger. When such an incident occurs, the database will store the Mac Addresss of both users, the RSSI strength that was reported,
and will utilize an geolocation API to store the longitiude, latitide and date/time of the incident.

Geolocation:





