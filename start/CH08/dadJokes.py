import requests

url = "https://icanhazdadjoke.com/"

payload={}
headers = {
  'accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

joke = response.json()["joke"]
print(joke)