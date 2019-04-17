import urllib.request
response = urllib.request.urlopen('https://www.google.com/')
print("<h3>" + str(response.read()) + "</h3>")
