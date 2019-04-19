from flask import Flask, request
import urllib.request
import requests
import time
from threading import Timer

 
app = Flask(__name__)
 
@app.route("/btn_find", methods=['POST'])
def get_ses():
    counter = 1
    number_of_repeats = int(request.form['number'])
    sleeping_time = float(request.form['sleeping'])
    s = request.form['text']
    link = s
    
    #response = urllib.request.urlopen(request.form['text'])    
    while number_of_repeats > 0:
        if (sleeping_time*(counter+1) > 25):
            break
        counter +=1
        number_of_repeats -= 1  
        send_request(link)
        print('#'*40)
        print(number_of_repeats)
        print('#'*40)        
        time.sleep(sleeping_time)
    
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Clicker chooser Online</title>
     <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
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
    <p align="center">
        <input name="submit" id="BTN" type="submit" value="Start">
    </p>
</form>

  <script>
   jQuery(document).ready(function() {
        
            $.ajax({
                url: '/btn_find',
                method: 'POST'
            });
    });
  </script>

</body>
</html>
'''
    if number_of_repeats <= 0:        
        return "Success"
    
    html = html.replace("{number_repeats}", str(number_of_repeats))
    html = html.replace("{link}", str(link))
    html = html.replace("{sleeping}", str(sleeping_time))
    #t = Timer(5.0, app.run)
    #t.start()
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
<h2 align="center">Welcome to the Clicker.online0001!</h2>
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
