import urllib.request
contents = urllib.request.urlopen("https://www.google.com").read()
print(contents)
