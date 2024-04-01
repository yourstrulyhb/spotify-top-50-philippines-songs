""" 
Top 50 Songs PH

Get Spotify Top 50 songs Philippines per week

https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

python -m flask --app .\app\app.py run
python -m flask run

set FLASK_APP=app
set FLASK_ENV=development
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
   # return "Hello World, from Flask!"
   return render_template('index.html')

