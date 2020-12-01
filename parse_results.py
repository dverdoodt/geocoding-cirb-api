# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:47:56 2020

@author: dverdoodt
@description: function to get the best address
"""
def getBestAddress(data):
    """data is JSON-formatted address information. Direct return from the API call"""
    best_score = 0
    best_street = None
    best_number = None
    best_postal_code = None
    best_municipality = None
    try:
        for i in range(len(data['result'])):
            score = data['result'][i]['score']
            street = data['result'][i]['address']['street']['name']
            number = data['result'][i]['address']['number']
            postal_code = data['result'][i]['address']['street']['postCode']
            municipality = data['result'][i]['address']['street']['municipality']

            if score >= best_score:
                best_score = score
                best_street = street
                best_number = number
                best_postal_code = postal_code
                best_municipality = municipality
    except:
        pass
        
    return best_score, best_street, best_number, best_postal_code, best_municipality