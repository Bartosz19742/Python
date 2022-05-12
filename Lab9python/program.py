# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:42:28 2022

@author: Bartosz
"""

import mojeklasy as mk

if __name__ == "__main__":
    f1 = mk.Punkt2D()
    print("Wartosci Punkt2D:")
    f1.Drukuj()
    f1.x1 = 10
    f1.y1 = 23
    print("Wartosci Punkt2D po zmianie:")
    f1.Drukuj()
    f1.Zeruj()
    print("wyzerowana wartość Punkt2D:")
    f1.Drukuj()

 
    f2 = mk.Punkt3D()

    print("Wartosci Punkt3D:")
    f2.Drukuj()
    f2.x1 = 11
    f2.y1 = 21
    f2.z = 24
    print("Wartosci Punkt3D po zmianie:")
    f2.Drukuj()
    f2.Zeruj()
    print("wyzerowana wartość Punkt3D:")
    f2.Drukuj()


    f3 = mk.Odcinek()
    f3.x1 = 3
    f3.x2 = 5
    f3.y1 = 12
    f3.y2 = 5
    f3.dlugosc()
    f3.drukuj()