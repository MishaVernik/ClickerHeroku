from flask import Flask, request
import urllib.request
import requests

app = Flask(__name__)


@app.route("/btn_find", methods=['POST'])
def get_ses():
    #response = urllib.request.urlopen(request.form['text'])
    r = requests.get(request.form['text'])
    return str(r.text)
        
            

@app.route('/')
def source():
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Clicker chooser Online</title>
</head>
<body>
<h2 align="center">Welcome to the Clicker.online!</h2>
<form method="POST" action="/btn_find">
    <p align="center">
        <input name="text" type="text" value="">
    </p>
    <p align="center">
        <input name="start" type="submit" value="Start">
    </p>
</form>
</body>
</html>
'''
    
    return html
