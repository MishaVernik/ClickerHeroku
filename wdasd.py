import urllib.request
import requests

import time
r = requests.get("http://google.com")
time.sleep(5)
print(r.text)
