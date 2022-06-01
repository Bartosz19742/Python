# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 14:32:57 2022

@author: Bartosz
"""

import sqlite3

if __name__ == "__main__":

    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    
    conn.execute('CREATE TABLE pracownicy (imienazwisko TEXT, nrpracownika TEXT, adres TEXT)')
    print("Tabela utworzona")
    
    conn.close()
    print("BD zamknieta")
    
    
    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    cur = conn.cursor()
    
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Bartosz Pisarek','1','Elbląg') )
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Karol Kucharski','2','Elbląg') )
    conn.commit()
    
    cur.execute('SELECT * FROM pracownicy ORDER BY nrpracownika')
    print(cur.fetchall())
    
    conn.close()
    print("BD zamknieta")