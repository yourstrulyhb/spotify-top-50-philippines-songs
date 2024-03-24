""" 
Get Spotify Top 50 songs Philippines - Data


https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

python -m flask --app .\app\app.py run
python -m flank run
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def home():
   # return "Hello World, from Flask!"
   return render_template('index.html')