# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:56:12 2022
@author: Melanie
"""

# Reads data from incoming POST-requests
# Finds the first 10 results in Google of a given keyword
# Startfunction main(request) will be called by endpoint POST-request handler

import json
from tld import get_tld

# Extracts keyword from body -> form-data from POST-request
# Input: unmodified Post-request
def read_Post_request(request): 
    read_keyword = request.form.get('keyword')  
    return read_keyword


# Searching for the first 10 google results of given keyword
# Input: String keyword
# Output: JSON Scheme: {'results': [{result_ID=1, url, tld}, ..., {result_ID=10, url, tld}]}
    # result_ID: position from top (1) to buttom (10)
    # url: google result website link
    # tld: top level domain
def google_results(keyword): 
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    current_position = 1
    object_list = []
    for j in search(keyword, tld="co.in", num=10, stop=10, pause=2):
        x = {'result_ID' : current_position, 'url' : j, 
             'tld' : get_tld(j)}
        object_list.append(x)
        current_position = current_position + 1
        
    outcome = {}
    outcome.update({"results" : object_list})   
    jsonStr = json.dumps(outcome)
    return jsonStr 

# Reads data from Post-request by method read_Post_request(request)
# Searchs keyword in Google by method google_results(read_keyword)
# Input: POST-request
# Return: Search results in jsonStr as a JSON string  
def main(request): 
    read_keyword = read_Post_request(request)
    if (not read_keyword):
        return "Data is missing"
    else:  
        jsonStr = google_results(read_keyword)
        return jsonStr
