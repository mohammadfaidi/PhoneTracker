#pip install phonenumber
#pip install phonenumbers
#pip install folium
import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

samNumber =phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber,"en")

print(yourLocation)

key = 'a78161dc2a89416d97dd5213b00387a1'
##Get services provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)

print(carrier.name_for_number(service_provider,"en"))

#pip install opencage

from opencage.geocoder import OpenCageGeocode



geocoder = OpenCageGeocode(key)
query = str(yourLocation)

result = geocoder.geocode(query)

print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)


myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourLocation).add_to((myMap))

myMap.save("mylocation.html")
