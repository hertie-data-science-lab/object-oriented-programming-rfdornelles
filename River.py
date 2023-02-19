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
       self._n_room = n_room
       print(f"Creating a River with {n_room} places.")

    def initialize(self):  
       print("Initializing the River...")
       n_room = self._n_room
       eco = self.eco
       
       # distribute bears, fishs and None thorugh
       # the river
       print("Populating the river")
       for room in range(n_room):
           # random choice
           random_room = np.random.choice([Bear(room), Fish(room), None])

           # add to the ecosystem
           eco.append(random_room)
       self.eco = eco
       print("River poulated with:")
       print("{:02d} Fishes | {:02d} Bears | {:02d} Empty spaces".format(len(self.where_is_creature("Fish")), len(self.where_is_creature("Bear")), len(self.where_is_creature("-"))))
       print("\n")
       
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        for room in range(len(self.eco)):
            print("Room {:02d} | {}".format(room, self.get_kind(room)))
        #print(self.eco, "\n")
        print("===================")
        
    # method to inform the positions of a specific kind
    def where_is_creature(self, kind):
        # create a empty list to be appended
        indexes = []
        
        for element in range(len(self.eco)):
            #print(type(self.eco[element]))
            if self.get_kind(element) == kind:
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
            return "-"
        else:
            return self.eco[element].kind 
    
    # method next_time_step - loop over iterations
    def next_time_step(self, iterations):

        counter = 1
    
        while counter <= iterations:
            print(f"Iteration {counter} of {iterations}")
            counter += 1
    # get all creatures
            animals = [] 
            for room in range(len(self.eco)):
                if self.get_kind(room) != "-":
                    animals.append(room)
            
            for room in animals:
                if np.random.choice([True, False]) == True: 
                    self.round(room)
                else:
                    print(f"      {self.get_kind(room)} at room {room} decided to stay.")

    def round(self, room):        
        # if in 0, only 1
        if room == 0:
            move_to = 1
        # if in the last, only the previus
        elif room == len(self.eco) -1:
            move_to = len(self.eco) -2
        else:
             # if not, then -1 and +1
            move_to = [room-1, room+1]
            move_to = np.random.choice(move_to)

        # check if the new room is empty
        # if not, they collide and stay in the place
        if self.eco[move_to] is None:
            print(f"      {self.get_kind(room)} at room {room} moved to {move_to}")
            self.eco[room].move(self, room, move_to)
            return
             
             # if they are from the same specie, generate
        if self.get_kind(room) == self.get_kind(move_to):
            self.eco[room].generate(self, self.get_kind(room))
            return
        
        else:
             # if they are different, kill the fish
            if self.get_kind(room) == "Fish":
             self.eco[room] = None
            else:
             self.eco[move_to] = None
