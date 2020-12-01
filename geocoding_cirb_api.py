# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:34:07 2020

@author: dverdoodt
@description: Use the geocoding API to geocode addresses in an Excel file.
Write the result to an Excel file.
"""

# Import modules
import requests
import pandas as pd
import parse_results


# Initialize variables
api_url = 'http://service.gis.irisnet.be/localization/Rest/Localize/getaddresses?'
input_file = "./input_addresses.xlsx"
output_file = './output_addresses.xlsx' 
sheet_name = "Site"
usecols = "D,E,F,G,H,I"
nrows = 10 # None. Use an integer to take a sample when testing

# Creat pandas dataframe
input_xls = pd.read_excel(io=input_file, sheet_name=sheet_name, header=0, usecols=usecols, nrows=nrows)

nRows, nCols = input_xls.shape

# Create empty lists to store geocoding results
id_sites = []
original_addresses = []
scores = []
streets = []
numbers = []
pcs = []
municipalities = []

# Loop over input addresses
for i in range(nRows):
    # Get id
    id_site = input_xls['ID - Site'][i]
    id_sites.append(id_site)
    ##print(id_site)
    
    # Get adress
    adress = input_xls['Address'][i]
    original_addresses.append(adress)
    ##print(adress)
    
    # Fill adress in parameters
    params= {'language': 'fr',
             'address': adress,
             'spatialReference': 31370}
    
    # Launch HTTP request (Geocoding)
    response = requests.get(api_url, params)
    
    # Format into JSON
    data = response.json()
    
    # Get address with best score 
    score, street, number, pc, municipality = parse_results.getBestAddress(data)
    ##print('Score {0}:\n{1} {2}, {3} {4}\n\n'.format(score, street, number, pc, municipality))

    # Append the results to lists
    scores.append(score)
    streets.append(street)
    numbers.append(number)
    pcs.append(pc)
    municipalities.append(municipality)
    
# Convert the lists to a dataframe
# Dictionnary containing all the data
data = {'id_site': id_sites,
        'original_address': original_addresses,
        'score':  scores,
        'street': streets,
        'number': numbers,
        'postal_code': pcs,
        'municipality': municipalities
        }

# Convert dictionnary to a pandas dataframe
df_geocoding = pd.DataFrame (data, columns = ['id_site','original_address', 'score','street','number','postal_code','municipality'])
# Sort by score descending
df_geocoding.sort_values(by=['score'], ascending=True)


# Write to Excel file
df_geocoding.to_excel(excel_writer=output_file,
                     sheet_name='geocoding_results',
                     float_format="%.2f",
                     index=False)