import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# ALPHA VANTAGE API
STOCK_API_KEY = "XXXXXXX"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS API
NEWS_API_KEY = "YYYYYY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
PAGE_SIZE = 3
# Twilio API
account_sid = "ZZZZZZZZ"
auth_token = "AAAAAAAA"

func_key = "Time Series (Daily)"
close_data = "4. close"

plus_minus = "🔺"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_params = {
       "q": COMPANY_NAME,
       "pageSize": PAGE_SIZE,
       "language": "en",
       "apiKey": NEWS_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

stock_date_data = [k for k, v in stock_data[func_key].items()]
yesterday_close = float(stock_data[func_key][stock_date_data[0]][close_data])
day_before_close = float(stock_data[func_key][stock_date_data[1]][close_data])

diff = yesterday_close - day_before_close
if diff < 0:
    diff *= -1
    plus_minus = "🔻"

diff_per = round((diff / day_before_close) * 100)

if diff_per >= 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_data_list = [(news_data["articles"][i]["title"],
                       news_data["articles"][i]["description"]) for i in range(PAGE_SIZE)]
    client = Client(account_sid, auth_token)
    for t, d in news_data_list:
        message = client.messages.create(
            body=f"Title: {t}\n\nBrief: {d}",
            from_='+123456',
            to='+123456787654'
            )
        print(message.status)
