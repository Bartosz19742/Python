# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:08:08 2022

@author: Student
"""

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def main():
 dane = {'tytul':'Strona główna','tresc':'Witaj na stronie glownej.'}
 return render_template('index.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route("/info")
def info():
 return render_template('info.html')

@app.route("/about")
def omnie():
 return render_template('Omnie.html')

if __name__ == '__main__':
 app.run(debug = True)
