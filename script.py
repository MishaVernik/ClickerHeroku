from flask import Flask, request
import urllib.request
import requests
import time
app = Flask(__name__)

counter = 1
number_of_repeats = 0

@app.route("/btn_find", methods=['POST'])
def get_ses():
    global counter    
    global number_of_repeats

    couter = 1
    number_of_repeats = int(request.form['number'])
    sleeping_time = float(request.form['sleeping'])
    s = request.form['text']
    #response = urllib.request.urlopen(request.form['text'])    
    while number_of_repeats > 0:
        if (sleeping_time*counter > 25):
            break
        counter +=1
        number_of_repeats -= 1  
        send_request(s)
        print('#'*40)
        print(i)
        print('#'*40)        
        time.sleep(sleeping_time)
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
        <input name="text" type="text" value="{link}">
    </p>
    <h3>Number of repeats</h3>
     <p align="center">
        <input name="number" type="text" value="{number_repeats}">
    </p>
    <h3>Sleeping time</h3>
     <p align="center">
        <input name="sleeping" type="text" value="{sleeping}">
    </p>
</form>
</body>
</html>
'''
    if number_of_repeats < 0:        
        return "Success"
    
    html = html.replace("{number_repeats}", str(number_of_repeats))
    html = html.replace("{link}", str(s))
    html = html.replace("{sleeping}", str(sleeping))
  
    return html
        
def send_request(s):
    try:            
        r = requests.get(s)
        r.raise_for_status()
        print('#'*40)
        print("YES")
        print('#'*40)     
        if r.status_code == 200:        
            return 1           
    except requests.exceptions.HTTPError as err:        
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
