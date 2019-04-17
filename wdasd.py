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

