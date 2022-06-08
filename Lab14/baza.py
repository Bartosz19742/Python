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
    
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Bartosz Pisare', '1', 'ul. Rpbotnicza 7/13, 82-300 Elblag') )
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Karol Kucharski', '2', 'ul. Grunwaldzka 2a/5, 82-300 Elblag') )
    conn.commit()
    
    cur.execute('SELECT * FROM pracownicy ORDER BY nrpracownika')
    print(cur.fetchall())
    
    conn.close()
    print("BD zamknieta")