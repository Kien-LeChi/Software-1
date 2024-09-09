# Access using Latitude and Longitude :
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#
# Access using municipality name :
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
#
# List of municipality :

import requests
import json

country = input("Enter your municipality (city): ")
country_api = ("https://api.openweathermap.org/data/2.5/weather?q="
               + country
               + "&limit=5&appid=fe076d38a7a7af9a836f793bfec86c9e&units=metric")

response = requests.get(country_api).json()

with open('ScratchOutput.txt', 'w') as file:
    file.write(json.dumps(response, indent = 4))
    file.write('\n\n#----------- END OF OUTPUT -----------#\n\n')

lat = str(response['coord']['lat'])
lon = str(response['coord']['lon'])

# print(lat, lon)
request = ("https://api.openweathermap.org/data/2.5/weather?lat="
           + lat + "&lon=" + lon
           + "&appid=fe076d38a7a7af9a836f793bfec86c9e&units=metric")
response = requests.get(request).json()

with open("ScratchOutput.txt", 'a') as file:
    file.write(json.dumps(response, indent = 4))

print(f"Today {country}'s weather is: {response['weather'][0]['description']}")
print(f"The temperature (in Celsius) is: {response['main']['temp'] :.2f}")