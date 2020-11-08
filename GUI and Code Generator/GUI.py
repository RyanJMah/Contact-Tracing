from tkinter import *
import sys
import os
<<<<<<< HEAD

<<<<<<< HEAD:GUI/file.py
=======
=======
import hashlib
>>>>>>> a117148a6c085399d32adc2753cb4130742c165a

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/database")
from sql import *

sys.path.insert(1, f"{PARENT_DIR}/geolocation")
from geo import *

>>>>>>> 0ec31723714de5eeef6e9cc0ebbe646ec1d835f4:GUI and Code Generator/GUI.py
class GUI :
    def __init__(self,master):
        self.Covid_Test_Code = ''
        self.Usermac_adr = ''
        self.close_contacts = 0
        root.geometry("300x150")

        #Text and Inputs
        self.Title = Label(root, text = "Contact Tracing V0.1", fg = "black")
        self.mac_adr = Entry(root)
        self.mac_adrLabel = Label(root, text = "Mac Address:", fg = "black")
        self.currentmac_adrLabel = Label(root, text = "Current Mac Address:", fg = "black")
        self.currentmac_adr = Label(root, text = self.Usermac_adr, fg = "black")
        self.StatusTitle = Label(root, text = "Status:", fg = "black")
        self.Status = Label(root, text = "Safe", fg = "green")
        self.TestCodeLabel = Label(root, text = "Positive Test Code: ", fg = "black")
        self.TestCode = Entry(root)
        self.TestCodeValidity = Label(root, text = "", fg = "black")
        self.Refresh = Button(root, text = "Refresh" , fg = "black", command = self.refresh)


        #Plotting each item
        self.Title.grid(column = 1 , sticky = W)
        self.StatusTitle.grid(row = 1, sticky = E)
        self.Status.grid(row = 1, column = 1, sticky = W)
        self.mac_adrLabel.grid(row = 2, sticky = E)
        self.mac_adr.grid(row = 2, column = 1, sticky = W)
        self.currentmac_adrLabel.grid(row = 3, sticky = E)
        self.currentmac_adr.grid(row = 3, column = 1, sticky = W)
        self.TestCodeLabel.grid(row = 4, sticky = E)
        self.TestCode.grid(row = 4, column = 1, sticky = W)
        self.TestCodeValidity.grid(row = 5, column = 0, columnspan = 2, sticky = E)
        self.Refresh.grid(row = 6 , column = 1, sticky = W )

        self.mac_adr.bind("<Return>" , self.Updatemac_adr)
        self.TestCode.bind("<Return>" , self.CheckCode)

    def Updatemac_adr(self,event):
        #User uptates their mac_adr
        if self.Usermac_adr == '':
            add_user(self.mac_adr.get(), 0)
        Update_mac_adr(self.Usermac_adr, self.mac_adr.get())
        self.Usermac_adr = self.mac_adr.get()
        self.currentmac_adr.config(text=self.Usermac_adr)
        code = hashlib.sha256(self.Usermac_adr.encode('utf-8'))
        self.Covid_Test_Code = code.hexdigest()

    def CheckCode(self,event):
        #Checks if the code is correct
        if self.Covid_Test_Code == '':
            self.TestCodeValidity.config(text="Please Provide Your Mac Address", fg = "red")
        elif self.TestCode.get() == str(self.Covid_Test_Code):
            self.TestCodeValidity.config(text="Code Valid, Warning Sent To " + str(self.close_contacts) + " Close Contacts", fg = "green")
            Update_user_covid_status(self.Usermac_adr, 1)

        else:
            self.TestCodeValidity.config(text="Incorrect Code", fg = "red")

    def Getmac_adr(self):
        return(self.Usermac_adr)

    def refresh(self):
        print("works")

    def UpdateStaus(self, stat = "Safe"):
        #Updates to tell the user if they're safe or not
        if stat == "Close Contact":
            self.Status.config(text="GET TESTED", fg = "red")
        else:
            self.Status.config(text="Safe", fg = "green")

root = Tk()
gui = GUI(root)
root.mainloop()
