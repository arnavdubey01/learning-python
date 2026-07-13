# 7. Explore the ‘Flaskʼ module and create a web server using Flask & Python.

# in terminal, enter:
# pip install flask

# Go on web, google search- flask module
# You'll find this https://flask.palletsprojects.com/
# Click on "A minimal Application" 
# (https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application)

# copy the code, paste:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# You can read instructoins on the website.

app.run()   #local web server is created





