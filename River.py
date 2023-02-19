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
           #print(self.eco)
       
    def initialize(self):  
       pass
       
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.eco, "\n")
        print("===================")
        
    # method to inform the positions of a specific kind
    def where_is_creature(self, kind):
        # create a empty list to be appended
        indexes = []
        
        for element in range(len(self.eco)):
            print(type(self.eco[element]))
            if type(self.eco[element]) == kind:
                indexes.append(element)
        
        return indexes
    
    # return where there's empty space in the river
    def where_is_empty(self):
        indexes = []
        
        for element in range(len(self.eco)):
            if self.eco[element] is None:
                indexes.append(element)
        
        return indexes
    
    # method get_kind
    def get_kind(self, element):
        
        room = self.eco[element]
        
        if room is None:
            return "Empty room"
        else:
            return self.eco[element].kind 
    
    # method set_content_index
     
    # method next_time_step - loop over iterations
    
    