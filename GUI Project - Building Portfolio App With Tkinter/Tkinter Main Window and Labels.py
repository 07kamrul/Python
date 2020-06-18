from tkinter import *
import requests
import json

pycrpto = Tk()
pycrpto.title("My Crypto Portfolio")
pycrpto.iconbitmap('favicon.ico')

def font_color(amount):
    if amount >= 0:
        return "green"

    else:
        return "red"

def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=3889ce63-c733-403d-8b7d-c41a2438b4ea")

    api = json.loads(api_request.content)

    print("------------------")
    print("------------------")

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
        },
        {
            "symbol": "XMR",
            "amount_owned": 10,
            "price_per_coin": 40.05
        }
    ]

    total_pl = 0
    total_current_value = 0
    coin_row = 1

    for i in range(0, 300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_percoin * coin["amount_owned"]

                total_pl = total_pl + total_pl_coin
                total_current_value = total_current_value + current_value

                name = Label(pycrpto, text=api["data"][i]["symbol"], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(pycrpto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                no_coin = Label(pycrpto, text=coin["amount_owned"], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
                no_coin.grid(row=coin_row, column=2, sticky=N + S + E + W)

                amount_paid = Label(pycrpto, text="${0:.2f}".format(total_paid), bg="#F3F4F6",fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_val = Label(pycrpto,text="${0:.2f}".format(current_value), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
                current_val.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_coin = Label(pycrpto, text="${0:.2f}".format(pl_percoin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(pl_percoin))), font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
                pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                totalplcoin = Label(pycrpto, text="${0:.2f}".format(total_pl_coin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl_coin))), font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
                totalplcoin.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row = coin_row + 1

    totalcv = Label(pycrpto, text="${0:.2f}".format(total_current_value), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2"))
    totalcv.grid(row=coin_row, column=6, sticky=N + S + E + W)

    totalpl = Label(pycrpto, text="${0:.2f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl))),font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2"))
    totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

            print(api["data"][i]["name"] + "-" + api["data"][i]["symbol"])
                print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                print("Number of Coin: ", coin["amount_owned"])
                print("Total Amount Paid: ", "${0:.2f}".format(total_paid))
                print("Currnt Value: ", "${0:.2f}".format(current_value))
                print("P/L Per Coin: ", "{0:.2f}".format(pl_percoin))
                print("Total P/L with Coin: ", "${0:.2f}".format(total_pl_coin))
                print("-----------")

    print("Total P/L for Portfolio: ", "${0:.2f}".format(total_pl))



name = Label(pycrpto, text="Price",bg="black", fg="white")
name.grid(row=0, column=1, sticky=N+S+E+W)

name = Label(pycrpto, text="Coin Owned",bg="black", fg="white")
name.grid(row=0, column=2, sticky=N+S+E+W)

name = Label(pycrpto, text="Total Amount Paid",bg="black", fg="white")
name.grid(row=0, column=3, sticky=N+S+E+W)

name = Label(pycrpto, text="Current Value",bg="black", fg="white")
name.grid(row=0, column=4, sticky=N+S+E+W)

name = Label(pycrpto, text="P/L Per Coin",bg="black", fg="white")
name.grid(row=0, column=5, sticky=N+S+E+W)

name = Label(pycrpto, text="Total P/L with Coin",bg="black", fg="white")
name.grid(row=0, column=6, sticky=N+S+E+W)

pycrpto.mainloop()

print("Program Complete")
