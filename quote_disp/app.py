from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

@app.route("/health")
def health():
    return int(200)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get_quote")
def get_quote():

    quote = requests.get('http://gen:5000/quote')
    print('quote - ', quote)

    return render_template('quote.html', quote = quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)