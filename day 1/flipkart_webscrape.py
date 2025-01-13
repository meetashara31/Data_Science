from bs4 import BeautifulSoup
import csv
import requests , pandas as pd
product_name=[]
product_price=[]
rating=[]

for i in range(0,10):
     
    url="https://www.flipkart.com/search?q=oppo%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
    
    r=requests.get(url)
    
    soup= BeautifulSoup(r.text,'lxml')
    
    box=soup.find('div',class_="DOjaWF gdgoEp")

    names = box.find_all("div",class_="KzDlHZ") 
        #print (names) 
    for i in names: 
        name=r.text
        product_name.append(name)
    print(product_name)


    prices = box.find_all("div",class_="Nx9bqj _4b5DiR") 
    for i in prices: 
        name=r.text
        product_price.append(name)
    print(product_price)

    # rating = box.find_all("div",class_="_5OesEi")
    # for i in rating:
    #     name=r.text
    #     rating.append(name)
    # print(rating)                    