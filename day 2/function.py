

# # Initialize empty lists to store product details
# product_name = []
# product_price = []
# product_rating = []

# for i in range(0, 10):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'lxml')

#     # Find the main container box
#     box = soup.find('div', class_="DOjaWF gdgoEp")

#     # Extract product names
#     names = box.find_all("div", class_="KzDlHZ")
#     for name in names:
#         product_name.append(name.text)

#     # # Extract product prices
#     prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
#     for price in prices:
#         product_price.append(price.text)

#     # Extract product ratings
#     ratings = box.find_all("div", class_="XQDdHH")
#     for rating in ratings:
#         product_rating.append(rating.text)

# df = pd.DataFrame({"product_name":product_name,"product_price":product_price,"product_rating":product_rating}) 
# # print (df)
# # df.to_csv("A:/work space/flipkart_oppo_data.csv")
# # print('created')
# print(df.columns)


#functoin
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import lxml


def Enter_Url(url,element):
    print(url)
    r= requests.get(url)
    soup=BeautifulSoup(r.text,'lmxl')
    box = soup.find(element)
    return box 
    
Enter_Url("https://webscraper.io/test-sites/e-commerce/allinone",'jumbotron')