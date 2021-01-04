# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:15:36 2020


@author: dverdoodt

Connect to a Python API with authentication


"""

import requests

# Verouderde? API
## http://service.gis.irisnet.be/localization/Rest/Localize/getaddresses?


# API without authentication
api = 'http://geoservices.irisnet.be/localization/Rest/Localize/getaddresses?'
params= {'language': 'fr', 'address': 'Rue de Namur 59 1000 Bruxelles', 'spatialReference': 31370}

r = requests.get(api, params)

print(r.status_code)
print(r.json())


## Api from api.brussels - smart.city
api = 'https://api.brussels:443/api/gla/0.0.1/getaddressses?'
params= {'language': 'fr', 'address': 'Rue de Namur 59 1000 Bruxelles', 'spatialReference': 31370}
headers = {
            "Accept": "application/json",
            "Authorization": "Bearer c7889f77-8fd2-336f-9eef-2353caf34ad1"
            }

r = requests.get(api, params, headers=headers)

print(r.status_code)

print(r.text)

print(r.json())