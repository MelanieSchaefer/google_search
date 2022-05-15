# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:33:43 2022
@author: Melanie
"""

# Creates an endpoint to handle GET- and POST-requests
# Handles authorization

import app_google_results
import jwt
import datetime
from flask import Flask, jsonify, request, make_response
from flask import request
from functools import wraps

# Create a flask (web) application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

def token_required(f): 
    @wraps(f)
    def decorated(*args, **kwargs): 
        token = request.args.get('Token') 
        if not token:
            return jsonify({'message': 'Token is missing!', 'request' : request}), 401
        
        try: 
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except: 
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/login')
def login(): 
    auth = request.authorization
    
    if auth and auth.password == 'password': 
        token = jwt.encode({'user': auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm=!Login required"'})

# Process incoming GET- and POST-requests
# IP: 127.0.0.1, Port: 5000  
@app.route('/', methods=['GET', 'POST'])
@token_required
def request_handler():
    if request.method == 'POST':
        google_results = app_google_results.main(request)
        return google_results 
    elif request.method == 'GET': 
        return jsonify({'message': 'Welcome! This was a GET-request'})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  
