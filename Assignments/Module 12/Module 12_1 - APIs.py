import requests

response = requests.get("https://api.chucknorris.io/jokes/random").json()
print(response['value'])