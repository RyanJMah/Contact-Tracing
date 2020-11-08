# Contact-Tracing
Prototype contact tracing app for hackathon

Names: Yahya Al-Shamali, 
       Roberto Villarreal Andrade, 
       Ryan Mah, 
       Norman Zhang
       
Date: November 7-8, 2020


Running Instructions:
To run this program, download all dependencies in "requirements.txt" using pip. You will also need to be running linux, and have the "bluetoothctl"
utility installed.

To run the Bluetooth scanner, cd into "BLE_Scanner" and run "report_incidents.py". To run the GUI, cd into "GUI and Code Generator" and run "GUI.py".


GUI.py:
Once the program is run, a GUI will pop up
The status indicates whether the user was in close contact with someone who has been tested positive for covid-19.
The status updates every 60 seconds. The user could also update their status instantly by clicking the Refresh Status button located at the bottom of the GUI.
Your mac address is required so that the program can identify you. The mac address will be stored in a database.
If you update your mac address, it will be updated in the database as well. The user's current mac address is shown under the input text box.
If the user tests positive, their tester will provide them with a positive test code. Once the code is inputted into the GUI, the database will update and will notify everyone who was in close contact. This test code is for making sure that all cases reported are guaranteed to be correct for security purposes.


Code Generator.py: 
This program asks for the user's mac address then it will return the positive test code. Only qualified testing professionals are allowed access to this code generator.


Database (sql.py):
A Google Cloud SQL database is used to store data of users and incidents. The database is composed of two tables, a users table and an incidents table. 
The users table stores the mac addresses of the user’s device along with a Boolean representing the users covid test results. If there are no test results, the default value is False.
The incidents table stores data on incidents where people are 6-feet or closer. When such an incident occurs, the database will store the mac addresses of both users, the RSSI strength that was reported,
and will utilize a geolocation API to store the latitude, longitude, and date/time of the incident. The database can add users, add incidents, update the user's covid status, update the mac address, and provide a list of people that a user has been in contact with.


Geolocation (geo.py):
A Geolocation REST API is used to report important information when an incident occurs. The following API was used: https://ipgeolocation.io/

The data taken from the API includes the user's longitude, latitude and time of incident. When an incident occurs. An http request is made to the API. The json data which is returned by the API is converted to a dictionary, which is then transferred to the SQL database.


BLE Scanner:
The BLE Scanner uses the Linux utility "bluetoothctl" to poll nearby Bluetooth devices for their mac address and instantaneous RSSI in dBm. How it achieves this, is it opens a subprocess which calls the following command using the "subprocess" module in the Python standard library:
       
       "bluetoothctl scan on"
       
It then reads from the standard output of the subprocess via a subprocess PIPE object, parses the output, and converts it into a dictionary of mac addresses and RSSI values.

The mac address and RSSI data are fed into the script "report_incidents.py", which runs in an infinite loop and reports an incident to the database when the RSSI of another device is within a certain threshold (>-70 dBm).
