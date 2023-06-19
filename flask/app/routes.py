from app import app

from flask import render_template

@app.route('/')
def land():
    return render_template('index.html')

@app.route('/favorite5')
def favorite5():
    athletes = [
        {
            'name':'Tom Brady',
            'sport':'Football',
            'position':'Quarterback'
        },
        {
            'name':'Rob Gronkowski',
            'sport':'Football',
            'position':'Tight End'
        },
        {
            'name':'David Ortiz',
            'sport':'Baseball',
            'position':'Designated Hitter'
        },
        {
            'name':'Kevin Garnett',
            'sport':'Basketball',
            'position':'Power Forward'
        },
        {
            'name':'Manny Ramirez',
            'sport':'Baseball',
            'position':'Outfield'
        }
    ]
    return render_template('favorite5.html', fave5=athletes)


    

