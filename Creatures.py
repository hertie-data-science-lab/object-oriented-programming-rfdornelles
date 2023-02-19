# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""

from abc import ABCMeta, abstractmethod
import numpy as np

class Creature(metaclass=ABCMeta):
    
    # define attribute position
    def __init__(self, position):
       # print("class", self.__class__)
        self.position = position
        # print("pos", self.position)
    
    # method move
    def move (self, river, current_position, new_position):
        
        if new_position < 0 or new_position > len(river.eco)-1:
            print("Impossible moviment")
            return False
        
        if river.eco[current_position] is None:
            print("Impossible to move empty space!")
            return False
        
        river.eco[new_position] = river.eco[current_position]
        river.eco[new_position].position = new_position
        
        river.eco[current_position] = None
        
        return True
        
    # method generate
    def generate(self, river, kind):
        # check which places are empty
        # any empty, stop
        # placed random where there's None 
        # new instance of same animal
        available_places = river.where_is_empty()
        
        print(f"      Two {kind} met and might generate other specime.")
        
        if len(available_places) == 0:
            print(f"Unfortunatelly, there's no free space.")
            return False
        
        random_place = np.random.choice(available_places)
        
        if kind == "Bear":
            river.eco[random_place] = Bear(random_place)  
        else:
            river.eco[random_place] = Fish(random_place)
        
        print(f"      {kind} geneated at room {random_place}!")    
        return True

        
class Bear(Creature):
   def __init__(self, position):
       super().__init__(position)
       self.kind = "Bear"

class Fish(Creature):
    def __init__(self, position):
        super().__init__(position)
        self.kind = "Fish"