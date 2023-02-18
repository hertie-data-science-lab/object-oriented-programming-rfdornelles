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
        self._position = position
    
    
    # method move
    
    # method generate
        # new instance of same animal
        # check which places are empty
        # any empty, stop
        # placed random where there's None 
        
class Bear(Creature):
    pass
 
        
class Fish(Creature):
    pass
