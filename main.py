import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=25.927530000000047&lon=-80.22214999999994#.XwNcSG1KjIU')

soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id = 'seven-day-forecast-body') 

items = week.find_all(class_ = 'tombstone-container')


period_names = [item.find(class_ = 'period-name').get_text() for item in items]
descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
temperatures = [item.find(class_ = 'temp').get_text() for item in items]

#print(period_names)
#print(descriptions)
#print(temperatures)

weather_stuff = pd.DataFrame(
  {
    'period':period_names,
    'short_description':descriptions,
    'temperatures':temperatures,
  })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')