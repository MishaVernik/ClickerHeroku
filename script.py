from flask import Flask

app = Flask(__name__)

@app.route('/')
def source():
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Route chooser Online</title>
</head>
<body>
<h2 align="center">Welcome to the railway.online!</h2>
<form method="post" action="btn_add_person">
    <p align="center">
        <input type="submit" value="Add person">
    </p>
</form>
<form method="post" action="btn_add_route">
    <p align="center">
        <input type="submit" value="Add route">
    </p>
</form>
<form method="post" action="btn_find_route">
    <p align="center">
        <input type="submit" value="Find route">
    </p>
</form>
</body>
</html>
'''
    return html
