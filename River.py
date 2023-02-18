# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
import numpy as np
from Creatures import Bear
from Creatures import Fish

class River:
    
    def __init__(self, n_room = 5):
       # create an ecosystem in the size n_room
       self.eco = []
       
       # distribute bears, fishs and None thorugh
       # the river
       for room in range(n_room):
           
           # random choice
           random_room = np.random.choice([Bear(room), Fish(room), None])
           
           # add to the ecosystem
           self.eco.append(random_room)
           
           #debug:
           print(self.eco)
       
    def initialize(self):  
       pass
       
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.eco, "\n")
        print("===================")
        
    # method inform_content_index
    
    
    # method set_content_index
    
    # method filter indexes
    
    # method eco
    
    # method next_time_step - loop over iterations
    
    