from app import app

from flask import render_template

@app.route('/')
def land():
    return render_template('index.html')

@app.route('/favorite5')
def home():
    return render_template('favorite5.html')


    

