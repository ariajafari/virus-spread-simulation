import matplotlib as plt
from numpy import random
#here we make coupled integer random number

class Person:
    def __init__(self,ID,Family_ID,Friend_ID,Health_Status):
        self.ID=ID 
        self.Family_ID=Family_ID
        self.Friend_ID=Friend_ID
        self.Health_Status=Health_Status
    def check_health(self):
        print(self.ID,self.Health_Status)

P1= Person(10,2,36,"h")
P1.check_health()