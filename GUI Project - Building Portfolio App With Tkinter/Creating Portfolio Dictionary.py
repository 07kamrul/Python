import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=3889ce63-c733-403d-8b7d-c41a2438b4ea")

api = json.loads(api_request.content)

# print(api)

coins = [
    {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 3200
    },
    {
        "symbol": "ETH",
        "amount_owned": 100,
        "price_per_coin": 2.05
    }
]

# print(api["data"][0]["symbol"])
# print(api["data"][0]["quote"]["USD"]["price"])

for i in range(0,5):
    for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:
            print(api["data"][i]["symbol"])
            print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("-----------")