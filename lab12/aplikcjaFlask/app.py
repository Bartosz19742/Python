# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:08:08 2022

@author: Student
"""

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def main():
 return render_template('index.html')

@app.route("/info")
def info():
 dane = {'tytul':'Info o mnie','tresc':'To jest informacja o mnie.'}
 return render_template('index.html', tytul=dane['tytul'], tresc=dane['tresc'])


@app.route("/about")
def omnie():
 return render_template('Omnie.html')

if __name__ == '__main__':
 app.run(debug = True)
