import matplotlib as plt
import numpy as np 

l=np.arange(25000)
list_of_families = l.reshape(5000, 5).tolist()
np.random.shuffle(l)
lisit_of_friends = np.reshape(l,(12500,2)).tolist()
list_of_persons=np.zeros((5000, 5)).tolist()

class Person:
    def __init__(self,ID,Family_ID,Friend_ID,Health_Status):
        self.ID=ID 
        self.Family_ID=Family_ID
        self.Friend_ID=Friend_ID
        self.Health_Status=Health_Status
    def check_health(self):
        print(self.ID,self.Health_Status)