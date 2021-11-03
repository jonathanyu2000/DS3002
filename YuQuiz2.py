# Jonathan Yu
# ComputingID: jxy7du

import requests
import csv
import time

apikey='TpDU0UFqxP5VJOgKDj9TpaC18LshL0bN6nIs96Pm'


url = "https://yfapi.net/v6/finance/quote"
stocksymbol = input("Please type stock symbol: ")
querystring = {"symbols": stocksymbol}
headers = {
  'x-api-key': apikey
   }

response = requests.request("GET", url, headers=headers, params=querystring)
response.raise_for_status()  # raises exception when not a 2xx response

if response.status_code != 204:
    stock_json = response.json()
    data_file = open("stockinfo.csv", 'a', newline = '')
    rows = [[str(stock_json['quoteResponse']['result'][0]["symbol"]),
            str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime((stock_json['quoteResponse']['result'][0]["regularMarketTime"])))),
            str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"])]]
    csvwriter = csv.writer(data_file)
    csvwriter.writerows(rows)
    print(stock_json['quoteResponse']['result'][0]["shortName"] + "\n"
          "Price:$" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]) + "\n"
          "Market Time: " + str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime((stock_json['quoteResponse']['result'][0]["regularMarketTime"])))
))
else:
    stocksymbol = input("Please enter a valid Stock Ticker: ")
