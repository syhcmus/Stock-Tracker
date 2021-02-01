import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla inct"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_APIKEY = 'O5783LI6SG04XCYO'
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_APIKEY
}

stock_data_json = requests.get(STOCK_ENDPOINT, params=stock_params).json()
stock_data = [value for (key, value) in stock_data_json['Time Series (Daily)'].items()]
stock_data_date = [key for (key, value) in stock_data_json['Time Series (Daily)'].items()]


NUMBER_ARTICLES = 3
NEWS_APIKEY = '27afb1eb4e32457580f4aceed6b729cb'
news_params = {

    'q': COMPANY_NAME,
    'from': stock_data_date[0],
    'sortBy': 'pulishedAt',
    'apiKey': NEWS_APIKEY

}


yesterday_closing_stock_price = float(stock_data[0]['4. close'])


the_day_before_yesterday_closing_stock_price = float(stock_data[1]['4. close'])

positive_difference = abs(yesterday_closing_stock_price - the_day_before_yesterday_closing_stock_price)


percentage_difference = positive_difference/the_day_before_yesterday_closing_stock_price*100


is_get_news = False
if percentage_difference > 5:
    is_get_news = True
    print('Get News')

    news_data_json = requests.get(NEWS_ENDPOINT, params=news_params).json()
    articles = news_data_json['articles'][:3]
    for article in articles:
        print(f"{article['title']}\n{article['url']}", end='\n\n')




