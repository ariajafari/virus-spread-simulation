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

def index_2d(mylist, v):
    for i, x in enumerate(mylist):
        if v in x:
            return ([i, x.index(v)])

k=0
for i in range(0,5000):
    for j in range(0,5):
        a=index_2d(lisit_of_friends,k)
        b=a[0]
        if  a[1]==1:
            f=lisit_of_friends[b][0]
        else:
            f=lisit_of_friends[b][1]
        x=index_2d(list_of_families,f)
        list_of_persons[i][j]=Person(k,i,x,"Healthy")
        k=k+1

list_of_persons[2][3].Health_Status="Infected"