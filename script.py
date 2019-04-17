import urllib.request
contents = urllib.request.urlopen("http://example.com/foo/bar").read()
print("<h3>" + contents + "</h3>")
