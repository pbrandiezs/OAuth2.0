#!/usr/bin/env python

from geocode import getGeocodeLocation
import json
import requests
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

#foursquare_client_id = "PASTE_YOUR_ID_HERE"
#foursquare_client_secret = "YOUR_SECRET_HERE"


def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url	
    
    # Get latitude and longitude
    latitude, longitude = getGeocodeLocation(location)
    # print(latitude, longitude)

    #Find a nearby restaurant from latitude and longitude, and mealType from the foursquare API
    ll = str(latitude) + "," + str(longitude)
    print("ll is: ",ll)
    print("\n\n")
    
    foursquare_client_id = "SM5SF3DDUN3XLAUDKQIHMPH5ON3DF3SD5XDELKQBGF1ZBRDI"
    foursquare_client_secret = "BBDZHLHTTQYTPJ5GTA5VRZ35CPQ4H4IP5OD2MTLR0GCKZBQ4"
    url = 'https://api.foursquare.com/v2/venues/explore'

    params = dict(
    client_id=foursquare_client_id,
    client_secret=foursquare_client_secret,
    v='20180323',
    ll=ll,
    query=mealType,
    limit=1
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    print(json.dumps(data, indent=4))
    print("\n\n")
    # Get restaurant name
    restaurant = data['response']['groups'][0]['items'][0]['venue']['name']

    print(restaurant)
    
    # Get venue_id
    venue_id = data['response']['groups'][0]['items'][0]['venue']['id']
    print(venue_id)
    # restaurant_image = data['response']['groups'][0]['items'][0]['venue']['name']



if __name__ == '__main__':
	# findARestaurant("Pizza", "Tokyo, Japan")
	# findARestaurant("Tacos", "Jakarta, Indonesia")
	# findARestaurant("Tapas", "Maputo, Mozambique")
	# findARestaurant("Falafel", "Cairo, Egypt")
	# findARestaurant("Spaghetti", "New Delhi, India")
	# findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	# findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney, Australia")