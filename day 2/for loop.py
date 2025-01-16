from bs4 import BeautifulSoup
import requests
import pandas as pd 

# Initialize empty lists to store product details
product_name = []
product_price = []
product_rating = []
url = "https://www.flipkart.com/search?q=oppo%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

for i in range(0, 10):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    
    box = soup.find('div', class_="DOjaWF gdgoEp")

   
    names = box.find_all("div", class_="KzDlHZ")
    for name in names:
        product_name.append(name.text)

   
    prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
    for price in prices:
        product_price.append(price.text)

    
    ratings = box.find_all("div", class_="XQDdHH")
    for rating in ratings:
        product_rating.append(rating.text)

df = pd.DataFrame({"product_name":product_name,"product_price":product_price,"product_rating":product_rating}) 
# print (df)
# df.to_csv("A:/work space/flipkart_oppo_data.csv")
# print('created')
print(df.columns)