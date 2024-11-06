import yfinance as yf
import pandas as pd
apple = yf.Ticker("AAPL")
import wget
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json'
wget.download(url, 'apple.json')
#Using the attribute info we can extract information about the stock as a Python dictionary.
import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable   
    #print("Type:", type(apple_info))
print(apple_info)
#We can get the 'country' using the key country
aic = apple_info['country']
print(aic)
##Extracting Share Price
#Using the period parameter we can set how far back from the present to get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
apple_share_price_data = apple.history(period="max")
print(apple_share_price_data)
#The format that the data is returned in is a Pandas DataFrame. With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
print(apple_share_price_data.head())
#We can reset the index of the DataFrame with the reset_index function. We also set the inplace paramter to True so the change takes place to the DataFrame itself.
print(apple_share_price_data.reset_index(inplace=True))
#We can plot the Open price against the Date:
print(apple_share_price_data.plot(x="Date", y="Open"))
##Extracting Dividends
print(apple.dividends)
#We can plot the dividends overtime:
print(apple.dividends.plot())
