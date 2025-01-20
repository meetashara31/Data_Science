from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.imdb.com/chart/top/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

# Find all the relevant span tags
y1= soup.find_all("h3", class_="ipc-title__text")
y = soup.find_all("span", class_="sc-300a8231-7 eaXxft cli-title-metadata-item")

data = [item.text for item in y]

# Separate into different lists
movie_name= [item.text for item in y1]
movie_name.pop(-1),movie_name.pop(0)

movie_year = []
movie_hours = []
movie_rate = []

for item in data:
    if item.isdigit() and len(item) == 4:  # Check if it's a year
        movie_year.append(item)
    elif 'h' in item and 'm' in item:  # Check if it's a duration
        movie_hours.append(item)
    elif len(item) <= 2 and item.isupper():  # Check if it's a rating
        movie_rate.append(item)

min_length = min(len(movie_name), len(movie_year), len(movie_hours), len(movie_rate))
movie_name = movie_name[:min_length]
movie_year = movie_year[:min_length]
movie_hours = movie_hours[:min_length]
movie_rate = movie_rate[:min_length]
# Converting list to the Dataframe
data=pd.DataFrame()
data['Movies']=movie_name
data['Hours']=movie_hours
data['Year']=movie_year
data['Rating']=movie_rate

data.to_csv("A:/work space/day 3/IMDB.csv")