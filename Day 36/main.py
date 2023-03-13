import requests as rq
import smtplib

MY_EMAIL = ""
TO_EMAIL = ""
PASSWORD = ""
MY_SMTP = ""
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = ""
STOCK_FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"
STOCK_API_END = "https://www.alphavantage.co/query"
STOCK_DATATYPE = "json"
PARAMETERS_STOCK = {
    "function": STOCK_FUNCTION,
    "symbol": STOCK,
    "datatype": STOCK_DATATYPE,
    "apikey": STOCK_API,
}
NEWS_API = ""
NEWS_API_END = "https://newsapi.org/v2/everything"
PARAMETERS_NEWS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API,
}


def main():
    response = rq.get(STOCK_API_END, params=PARAMETERS_STOCK)
    response.raise_for_status()
    data = response.json()['Time Series (Daily)']
    data_list = [value for (key, value) in data.items()]
    yesterday = float(data_list[0]['4. close'])
    day_before = float(data_list[1]['4. close'])
    change = ((yesterday-day_before)/yesterday)*100
    if change > 0:
        change_txt = f'UP {change:.02}%'
    else:
        change_txt = f'DOWN {change:.02}%'

    if abs(change) > 5:
        get_news(change_txt)
    else:
        email = f"Subject: {STOCK} Change\n\n" \
               f"{STOCK} -- {change_txt}"
        mail(email)


def get_news(change: str):
    request = rq.get(NEWS_API_END, params=PARAMETERS_NEWS)
    request.raise_for_status()
    news_data = request.json()['articles'][:3]
    for x in range(0, 3):
        email = f"Subect: {STOCK} Alert!\n\n" \
                f"{STOCK} -- {change}\n" \
                f"Source: {news_data[x]['source']['name']}\n" \
                f"Story: {news_data[x]['title']}\n" \
                f"Date: {news_data[x]['publishedAt']}\n" \
                f"URL: {news_data[x]['url']}\n"
        mail(email)

def mail(input):
    if MY_EMAIL == "" or PASSWORD == "" or TO_EMAIL == "":
        print(input)
    else:
        with smtplib.SMTP(MY_SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=input
            )

if __name__ == "__main__":
    main()
