import requests
from bs4 import BeautifulSoup
from mail import MailClient

PRICE_TO_BUY = 400

mail = MailClient()
amazon_url = "https://www.amazon.it/dp/B0931CK72M/ref=twister_B096KQ4XMW?_encoding=UTF8&th=1"
amazon_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
}
amazon_page = requests.get(amazon_url, headers=amazon_headers).text
amazon_soup = BeautifulSoup(amazon_page,"html.parser")
c_price = amazon_soup.find(name="span", id="priceblock_ourprice")
c_name = amazon_soup.find(name="span", id="productTitle")

price: float = float(c_price.getText().split()[0].replace(",",".",1))
item_name: str = c_name.getText()

if price < PRICE_TO_BUY:
    mail.set_message(price, item_name)
    mail.send_mail()
else:
    print("Price is too high")

