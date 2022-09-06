# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:52:07 2022

@author: Marcin
"""
#%%

from pprint import pprint

data_dict = {
    "users": [
        {
            "userId": 1,
            "firstName": "Krish",
            "lastName": "Lee",
            "emailAddress": "krish.lee@example.com"
        },
        {
            "userId": 2,
            "firstName": "racks",
            "lastName": "jacson",
            "emailAddress": "racks.jacson@example.com"
        },
        {
            "userId": 3,
            "firstName": "denial",
            "lastName": "roast",
            "emailAddress": "denial.roast@example.com"
        }
    ]
}
print (data_dict)
pprint (data_dict)

#%%
import requests
from pprint import pprint
 
def geocode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyBjt7LQnLuvTyVFB_WVrwlZAQwVBdSMdZ8n"
    resp = requests.get(url)
    return resp.json()
 
# calling geocode function
data = geocode('India gate')
 
# pretty-printing json response
pprint(data)