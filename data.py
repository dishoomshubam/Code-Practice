import requests

url = "https://amazon-price.p.rapidapi.com/azapi-allOffers"

querystring = {
    "page": "5",
    "asin": "B000GAYQKY",
    "marketplace": "US",
    "condition": "new",
}

headers = {
    "x-rapidapi-key": "7e78a116b2mshf5954bd9b5be164p1db1cajsn80bc6921a94e",
    "x-rapidapi-host": "amazon-price.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
