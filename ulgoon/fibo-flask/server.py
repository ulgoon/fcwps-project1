from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secret')
def get_secret():
    # get all the secrets from origin
    pass
    
if __name__=='__main__':
    app.run(host='localhost', port=4040, debug=True)
