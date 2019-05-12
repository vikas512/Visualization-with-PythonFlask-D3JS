# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:24:40 2017

@author: parevi02
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('FileCount.html')

if __name__ == '__main__':
    app.run(debug=True)