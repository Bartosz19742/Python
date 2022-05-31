# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:13:53 2022

@author: luqas
"""

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about_me():
    dane={'tytul':'Info o mnie','tresc':'To jest informacja o mnie.'}
    return render_template('omnie.html',tytul=dane['tytul'],tresc=dane['tresc'])

@app.route("/info")
def info():
    dane={'tytul':'Informacje ogolne','tresc':'Tu sa informacje ogolne'}
    posty=[
        {
            'author':{'username':'Lukasz'},
            'body': 'Jestem grafikiem'
        },
        {
            'author':{'username':'Przemek'},
            'body': 'Ja tez'
        }]
    return render_template('informacje.html',tytul=dane['tytul'],tresc=dane['tresc'],posty=posty)

if __name__ == "__main__":
    app.run()
