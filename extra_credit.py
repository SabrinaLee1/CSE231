# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:45:26 2023

@author: sabri
"""

import math

class Rocket:
    def __init__(self, x=0, y=0, name=1):
        self.x=x
        self.y=y
        self.name=name
    def move(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
    def get_distance(self, other_rocket):
        if isinstance(other_rocket, Rocket):
            dx = self.x - other_rocket.x
            dy = self.y - other_rocket.y
            return round(math.sqrt(dx**2+dy**2),4)
    def __str__(self):
        return f"Rocket {self.name} is at ({self.x},{self.y})"
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __gt__(self,other):
        return self.x**2 + self.y**2 > other.x**2 +other.y**2
    def __lt__(self,other):
        return self.x**2 + self.y**2 < other.x**2 + other.y**2
    
    
from myclass import Rocket
def main():
    rockets = [Rocket(0,0,0), Rocket(10,10,1), Rocket(10,0,2)]
    rockets[0].move(0,1)
    rockets[1].move(0,0)
    rockets[2].move(-20,0)
    print('\nShow where each rocket is:')
    for rocket in rockets:
        print(rocket)
    ranked = sorted(rockets, reverse=True)
    print('\nRank the rockets:')
    for rocket in ranked:
        print(rocket)

if __name__ == '__main__':
     main()
     
     
class PetError( ValueError ):
    pass

class Pet( object ):
    def __init__( self, species=None, name="" ):
        if species.lower() in ['dog', 'cat', 'horse', 'gerbil', 'hamster', 'ferret']:  
            self.species_str = species.title()
            self.name_str = name.title()    
        else:  
            raise PetError()      
    def __str__( self ): 
        if self.name_str:
            result_str = "Species of {:s}, named {:s}".format(self.species_str,self.name_str) 
        else:
            result_str ="Species of {:s}, unnamed".format(self.species_str)
        return result_str

class Dog( Pet ):
    def __init__(self, name='', chases='Cats'):
        Pet.__init__(self,"Dog", name)
        self.chases = chases
    def __str__(self):
        result_str = Pet.__str__(self)+", chases " +self.chases
        return result_str

class Cat( Pet ):
    def __init__(self, name='',  hates='Dogs'):
        Pet.__init__(self, "Cat", name)
        self.hates = hates
    def __str__(self):
        result_str = Pet.__str__(self)+", hates " +self.hates
        return result_str


import pets


def main():
    
    try:

        A = pets.Pet( "hamster" )
        print( A )
              
        # Dog named Fido who chases Cats
        B = pets.Dog( "Fido" )
        print( B )

        # Cat named Fluffy who hates everything
        C = pets.Cat( "Fluffy", "everything" )
        print( C )

        D = pets.Pet( "pig" )
        print( D )
        
    except pets.PetError:
        
        print( "Got a pet error." )

if __name__ == '__main__':
     main()
