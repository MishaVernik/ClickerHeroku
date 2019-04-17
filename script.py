from flask import Flask

app = Flask(__name__)

@app.route('/')
def source():
    with open("index.html", 'r') as f:
        html = f
        
    return html
