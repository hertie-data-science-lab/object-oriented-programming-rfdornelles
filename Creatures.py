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
        """Initialize setting the attribute position, 
        containing where in the River the creature ir

        Args:
            position (_type_): the numeric position
        """
        self.position = position

    
    # method move
    def move (self, river, current_position, new_position):
        """Move the creature along the river.

        Args:
            river (_type_): The River object.
            current_position (_type_): Where the creature is.
            new_position (_type_): To where the creature will go.
        """
        # if is a valid position
        if new_position < 0 or new_position > len(river.eco)-1:
            print("Impossible moviment")
            return False
        
        # avoid try to move a position without creatures
        if river.eco[current_position] is None:
            print("Impossible to move an empty space!")
            return False
        
        # copy the creture to the new position
        river.eco[new_position] = river.eco[current_position]
        # update the position
        river.eco[new_position].position = new_position
        
        # empity the original position
        river.eco[current_position] = None
        
        return True
        
    # method generate
    def generate(self, river, kind):
        """When two creatures met, a new specime is generated.
        This new creature will go to an empity space available.
        If there's no free space, then it will not be generated.

        Args:
            river (_type_): the River object
            kind (_type_): the kind ("Fish" or "Bear") that
            will be generaed
        """
        # check which places are empty
        available_places = river.where_is_empty()
        print(f"      Two {kind} met and might generate other specime.")
        
        # any empty, stop
        if len(available_places) == 0:
            print(f"Unfortunatelly, there's no free space.")
            return False
        
        # placed random where there's None 
        random_place = np.random.choice(available_places)
        
        # new instance of same animal
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