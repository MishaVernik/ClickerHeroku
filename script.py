from flask import Flask, request
import urllib.request
import requests
import time
app = Flask(__name__)

counter = 0

@app.route("/btn_find", methods=['POST'])
def get_ses():
    number_of_repeats = int(request.form['number'])
    sleeping_time = float(request.form['sleeping'])
    s = request.form['text']
    #response = urllib.request.urlopen(request.form['text'])    
    for i in range(number_of_repeats):
        
        send_request(s)
        print('#'*40)
        print(i)
        print('#'*40)        
        time.sleep(sleeping_time)
        
    return "Success!"
        
def send_request(s):
    try:
     r = requests.get(s)
     if r.status_code == 200:
         return 1
     else:
        raise ValueError
    except ValueError:       
        send_request(s)

 
    

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
    <h3>Link</h3>
    <p align="center">
        <input name="text" type="text" value="">
    </p>
    <h3>Number of repeats</h3>
     <p align="center">
        <input name="number" type="text" value="">
    </p>
    <h3>Sleeping time</h3>
     <p align="center">
        <input name="sleeping" type="text" value="">
    </p>
    <p align="center">
        <input name="start" type="submit" value="Start">
    </p>
</form>
</body>
</html>
'''
    
    return html
