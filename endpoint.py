# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:33:43 2022

@author: Melanie
"""

# Creates an endpoint to handle GET- and POST-requests

# For testing GET-request: starting this file and call http://127.0.0.1:5000 
# For testing POST-request: starting this file and send a POST-request
# according scheme: (url, data={'keyword': '', 'username': '', 'password': ''}) 
# for example with "Postman" https://www.postman.com/downloads/

import app_google_results
from flask import Flask
from flask import request

# Create a flask (web) application
app = Flask(__name__)

# Process incoming GET- and POST-requests
# IP: 127.0.0.1, Port: 5000  
@app.route('/', methods=['GET', 'POST'])
def request_handler():
    if request.method == 'POST':
        google_results = app_google_results.main(request)
        return google_results 
    elif request.method == 'GET': 
        return '''<h1>Welcome! This was a GET-request'''

if __name__ == '__main__':
    app.run(debug=True)  
