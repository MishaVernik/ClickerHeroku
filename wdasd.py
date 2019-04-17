import urllib.request
import requests

import time

def send_request(s):
    try:
     r = requests.get(s)
     if r.status_code == 200:
         return 1
     else:
         raise ValueError
    except ValueError:       
        send_request(s)

r = requests.get("http://google.com")
#time.sleep(5)
print(r.status_code)
if r.status_code == 200:
    print(r.status_code)

send_request("qwe")



   html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Clicker chooser Online</title>
</head>
<body>
<h2 align="center">Welcome to the Clicker.online!</h2>
<form method="POST" action="">
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
    html = html.replace("{sleeping}", str(sleeping_time))
  
    return html
