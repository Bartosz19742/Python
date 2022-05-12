# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:02:03 2022

@author: Bartosz
"""
import math as mh

def testy():
    pass
if __name__ == "__main__":
    testy()
    
class Punkt2D():
    x = 0
    y = 0
    
    def Drukuj(self):
        print("x = ",self.x,"y = ",self.y)
        
    def Zeruj(self):
        self.x=0
        self.y=0
        
class Punkt3D(Punkt2D):
    z = 0
    def Drukuj(self):
        print("x = ",self.x,"y = ",self.y,"z = ",self.z)
        
    def Zeruj(self):
        self.x=0
        self.y=0
        self.z=0
        
class Odcinek(Punkt2D):
    x2 = 0
    y2 = 0
    a = 0
    b = 0
    a1 = 0
    b1 = 0
    ab = 0
    
    def dlugosc(self):
        self.a = self.x2-self.x
        self.b = self.y2-self.y
        self.a1 = self.a*self.a
        self.b1 = self.b*self.b
        self.ab = mh.sqrt(self.a1+self.b1)
        
    def drukuj(self):
        print("Dlugosc odcinka wynosi: ",self.ab)
        
    
        
l = Punkt2D()
print("Wartosci Punkt2D:")
l.Drukuj()
l.x = 6
l.y = 10
print("Wartosci Punkt2D po zmianie:")
l.Drukuj()
l.Zeruj()
print("wyzerowana wartość Punkt2D:")
l.Drukuj()

l2 = Punkt3D()

print("Wartosci Punkt3D:")
l2.Drukuj()
l2.x = 71
l2.y = 31
l2.z = 26
print("Wartosci Punkt3D po zmianie:")
l2.Drukuj()
l2.Zeruj()
print("wyzerowana wartość Punkt3D:")
l2.Drukuj()


l3 = Odcinek()
l3.x = 3
l3.x2 = 5
l3.y = 16
l3.y2 = 0
l3.dlugosc()
l3.drukuj()

    