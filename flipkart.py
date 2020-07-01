 import requests
from bs4 import BeautifulSoup

URL = 'https://www.flipkart.com/mi-20000-mah-power-bank-pb20izm-18w-fast-charging/p/itm473a0523c0a6a?pid=PWBFGXKMW4UDPJUG&lid=LSTPWBFGXKMW4UDPJUG5FXUHB&marketplace=FLIPKART&spotlightTagId=BestsellerId_tyy%2F4mr%2Ffu6&srno=s_1_4&otracker=AS_QueryStore_OrganicAutoSuggest_0_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_10_na_na_na&fm=SEARCH&iid=41947c2a-aa82-4f0d-aee0-523443837fde.PWBFGXKMW4UDPJUG.SEARCH&ppt=sp&ppn=sp&ssid=yhog1w1sm80000001578665484671&qH=93838e3a65b51e46'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

price = soup.find(class_='_1vC4OE _3qQ9m1').get_text()
Title = soup.find(class_='_35KyD6').get_text()
print(Title)
# print(price) # This price is a string

converted_price = price[1:6]
final_price = float(converted_price.replace(",", ""))
# print(final_price)

if final_price < 1499:
    print("Price Dropped")
else:
    print(final_price)
