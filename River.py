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
        """Initialize the object River.

        Args:
            n_room (int, optional): size of the river. Defaults to 5.
        """
       # create an ecosystem in the size n_room
        self.eco = []
        self._n_room = n_room
        print(f"Creating a River with {n_room} places.")

    def initialize(self):  
        """Populate the river randomly. To each room in the river a specie (Bear or Fish) or a empty space will be chosen.
        """
        print("Initializing the River...")
        n_room = self._n_room
        eco = self.eco
       
       # distribute bears, fishs and None thorugh
       # the river
        print("Populating the river")
        # iterate through each room 
        for room in range(n_room):
           # random choice
           random_room = np.random.choice([Bear(room), Fish(room), None])

           # add to the ecosystem
           eco.append(random_room)
        
        # set the attribute in the River object
        self.eco = eco
        
        print("River poulated with:")
        print("{:02d} Fishes | {:02d} Bears | {:02d} Empty spaces".format(len(self.where_is_creature("Fish")), len(self.where_is_creature("Bear")), len(self.where_is_creature("-"))))
        print("\n")
       
    def display(self):
        """Show the current status of the ecosystem.
        """
        print("===================")
        print("Ecosystem status:")
        print("{:02d} Fishes | {:02d} Bears | {:02d} Empty spaces".format(len(self.where_is_creature("Fish")), len(self.where_is_creature("Bear")), len(self.where_is_creature("-"))))
        print("\n")
        
        for room in range(len(self.eco)):
            print("Room {:02d} | {}".format(room, self.get_kind(room)))
            
        print("===================")
        
    # method to inform the positions of a specific kind
    def where_is_creature(self, kind):
        """Find where the in the River there is the specif kind.

        Args:
            kind (_type_): Should be "Fish", "Bear" or "-" to empty space.

        Returns:
            _type_: A list containing the position where the rooms are.
        """
        # create a empty list to be appended
        indexes = []
        
        for element in range(len(self.eco)):
            if self.get_kind(element) == kind:
                indexes.append(element)
        
        return indexes
    
    # return where there's empty space in the river
    def where_is_empty(self):
        """Returns a list of empty spaces.

        Returns:
            _type_: A list with empty spaces, if any.
        """
        indexes = []
        
        for element in range(len(self.eco)):
            if self.eco[element] is None:
                indexes.append(element)
        
        return indexes
    
    # method get_kind
    def get_kind(self, element):
        """Inform the kind of the room.

        Args:
            element (_type_): The room number/the position in the ecosystem.

        Returns:
            _type_: The kind or "-"
        """
        room = self.eco[element]
        
        if room is None:
            return "-"
        else:
            # each animal has a attribute kind
            return self.eco[element].kind 
    
    # method next_time_step - loop over iterations
    def next_time_step(self, iterations):
        """Create interactions in the River.

        Args:
            iterations (_type_): Number of movements.
        """

        counter = 1
        # run while not reach the limit
        while counter <= iterations:
            print(f"Iteration {counter} of {iterations}")
            counter += 1
    # get all creatures
            animals = [] 
            for room in range(len(self.eco)):
                if self.get_kind(room) != "-":
                    animals.append(room)
            
            # check if is a valid creature
            for room in animals:
                if self.eco[room] is None:
                    continue
                
                # decide either stay or go, randomly
                if np.random.choice([True, False]) == True: 
                    # if go, run the method round
                    self.round(room)
                else:
                    print(f"      {self.get_kind(room)} at room {room} decided to stay.")

    def round(self, room):     
        """Function to move the animals. It try to move randomly to the adjacent space, generate nem specime when it's available or kill the fish when a Bear try to go to its place.
        """   
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
                # determine if the fish is in the current room or in the destiny
             self.eco[room] = None
             print(f"      Fish at room {room} died :(")
            else:
             self.eco[move_to] = None
             print(f"      Fish at room {move_to} died RIP!")
