from tkinter import *
import sys
import os

#Path to database directory

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/database")
from sql import *

sys.path.insert(1, f"{PARENT_DIR}/geolocation")
from geo import *

class GUI :
    def __init__(self,master):
        self.Covid_Test_Code = ''
        self.UserUUID = ''
        self.close_contacts = 0
        root.geometry("300x150")

        #Text and Inputs
        self.Title = Label(root, text = "Contact Tracing V0.1", fg = "black")
        self.UUID = Entry(root)
        self.uuidLabel = Label(root, text = "UUID:", fg = "black")
        self.currentUUIDLabel = Label(root, text = "Current UUID:", fg = "black")
        self.currentUUID = Label(root, text = self.UserUUID, fg = "black")
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
        self.uuidLabel.grid(row = 2, sticky = E)
        self.UUID.grid(row = 2, column = 1, sticky = W)
        self.currentUUIDLabel.grid(row = 3, sticky = E)
        self.currentUUID.grid(row = 3, column = 1, sticky = W)
        self.TestCodeLabel.grid(row = 4, sticky = E)
        self.TestCode.grid(row = 4, column = 1, sticky = W)
        self.TestCodeValidity.grid(row = 5, column = 0, columnspan = 2, sticky = E)
        self.Refresh.grid(row = 6)

        self.UUID.bind("<Return>" , self.UpdateUUID)
        self.TestCode.bind("<Return>" , self.CheckCode)

    def UpdateUUID(self,event):
        #User uptates their UUID
        self.UserUUID = self.UUID.get()
        self.currentUUID.config(text=self.UserUUID)
        self.Covid_Test_Code = hash(self.UserUUID)



    def CheckCode(self,event):
        #Checks if the code is correct
        if self.Covid_Test_Code == '':
            self.TestCodeValidity.config(text="Please Provide Your UUID", fg = "red")
        elif self.TestCode.get() == str(self.Covid_Test_Code):
            self.TestCodeValidity.config(text="Code Valid, Warning Sent To " + str(self.close_contacts) + " Close Contacts", fg = "green")
        else:
            self.TestCodeValidity.config(text="Incorrect Code", fg = "red")

    def GetUUID(self):
        return(self.UserUUID)

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
