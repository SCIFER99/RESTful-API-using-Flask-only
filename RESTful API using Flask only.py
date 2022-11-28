# By: Tim Tarver also known as CryptoKeyPlayer
# RESTful API using Flask only

# Using flask to make an API
# We must import necessary libraries and functions

from flask import Flask, jsonify, request

# This instantiates the Flask app

app = Flask(__name__)

# We connect to the terminal type: curl http://127.0.0.1:5000/
# This returns hello world when we use GET.
# Returns the data that we send when we use POST

@app.route('/', methods = ['GET', 'POST'])
def home():
    if (request.method == 'GET'):

        data = "hello world"
        return jsonify({'data' : data})

# This simple functions calculates the square of a number
# The number to be squared is sent to the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
    
@app.route('/home/<int:num>', methods = ['GET'])
def display(num):
    return jsonify({'data' : num**2})

#This is the driver function
if __name__ == '__main__':

    app.run(debug = True)
