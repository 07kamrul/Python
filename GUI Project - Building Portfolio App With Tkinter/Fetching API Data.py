import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=3889ce63-c733-403d-8b7d-c41a2438b4ea")

api = json.loads(api_request.content)

# print(api)

print(api["data"][0]["symbol"])
print(api["data"][0]["quote"]["USD"]["price"])