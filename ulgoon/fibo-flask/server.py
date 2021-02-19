from flask import Flask
from flask import request, render_template, redirect, url_for
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getfibo', methods=['POST'])
def get_fibo():
    if request.method=='POST':
        num = request.form['num']
        return redirect(url_for('show_result', num=num))

@app.route('/result')
def show_result():
    num = request.args['num']
    #base_uri = 'https://fibonachicken.herokuapp.com/?ajax=1&people='
    #complete_uri = base_uri + str(num)
    # get all the secrets from origin
    #return requests.get(complete_uri).text
    return num

if __name__=='__main__':
    app.run(host='localhost', port=4040, debug=True)
