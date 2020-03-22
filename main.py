import matplotlib as plt
import numpy as np 

l=np.arange(25000)
list_of_families = l.reshape(5000, 5).tolist()
np.random.shuffle(l)
lisit_of_friends = np.reshape(l,(12500,2)).tolist()
list_of_persons=np.zeros((5000, 5)).tolist()