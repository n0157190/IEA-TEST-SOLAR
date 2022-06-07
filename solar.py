#!/usr/bin/env python3
import requests
import time
from datetime import date, datetime
#import base64
from pprint import pprint   

def get_observer_location():
    """Returns the longitude and latitude for the location of this machine.
    Returns:str: latitude str: longitude"""
    url = 'http://ip-api.com/json/'
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    print('From '+ data['city']+ ' ' + data['region'] + ' at '+ time.strftime('%l:%M%p %Z on %b %d, %Y'))
    return data['lat'], data['lon']
    
def get_sun_position(latitude, longitude):
    ASTRONOMYAPI_ID = "d2580536-4710-46ac-9ae9-f2ac830466d5"
    ASTRONOMYAPI_SECRET = "70c87461360d7391d75797a5656eb5ad98801054accbe83edaa70b1e08f7a257236957b6280a183f88bdbbec494680c3e52077dcc422e2d4e9ee073d5a2dc497511b1438399c41440198d43a8572fda1e7c5aad328cbffbdfc5ae72531de6ab2077d437b3fd5634152e0891593b114d2"

    """Returns the current position of the sun in the sky at the specified location
    Parameters:
    latitude (str)
    longitude (str)
    
    Returns:
    float: azimuth
    float: altitude
    "https://api.astronomyapi.com/api/v2/bodies/positions/?latitude=43.0443&longitude=-70.4528&elevation=2&from_date=2022-05-16&to_date=2022-05-17&time=08:00:00"
    """
    today = date.today()
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    url = 'https://api.astronomyapi.com/api/v2/bodies/positions?latitude='+ str(latitude) +'&longitude='+ str(longitude) + '&elevation=2&from_date='+ str(today) +'&to_date='+ str(today) +'&time='+time
    #print('URL::: ',url)
    payload={}
    headers = {   'Authorization': 'Basic: ZDI1ODA1MzYtNDcxMC00NmFjLTlhZTktZjJhYzgzMDQ2NmQ1OjcwYzg3NDYxMzYwZDczOTFkNzU3OTdhNTY1NmViNWFkOTg4MDEwNTRhY2NiZTgzZWRhYTcwYjFlMDhmN2EyNTcyMzY5NTdiNjI4MGExODNmODhiZGJiZWM0OTQ2ODBjM2U1MjA3N2RjYzQyMmUyZDRlOWVlMDczZDVhMmRjNDk3NTExYjE0MzgzOTljNDE0NDAxOThkNDNhODU3MmZkYTFlN2M1YWFkMzI4Y2JmZmJkZmM1YWU3MjUzMWRlNmFiMjA3N2Q0MzdiM2ZkNTYzNDE1MmUwODkxNTkzYjExNGQy'}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        print('No connection ********* STATUS CODE: ',response.status_code, ' ', response.reason)

    data = response.json()
    #print(data.keys())
    for record in data['data']['table']['rows']:
        if record['cells'][0]['id'] == 'sun':
            #pprint(record['cells'][0]['position']['horizonal']['azimuth'])
            azimuth = record['cells'][0]['position']['horizonal']['azimuth']['degrees']
            altitude = record['cells'][0]['position']['horizonal']['altitude']['degrees']
            distance = record['cells'][0]['distance']['fromEarth']['km']
            print('Sun: Distance from Earth: '+ distance + ' km')
    return azimuth, altitude
    
def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates

    Parameters:
    azimuth (float)
    altitude (float)
    """
    print("The Sun is currently at: "+ azimuth +' degrees azimuth '+ altitude + ' degrees altitude')
    
if __name__== "__main__":
    latitude, longitude = get_observer_location()
    azimuth, altitude = get_sun_position(latitude, longitude)
    print_position(azimuth, altitude)