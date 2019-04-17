import urllib.request
response = urllib.request.urlopen('https://www.google.com/')
print(response.read())
while True:
    print("Hello")
