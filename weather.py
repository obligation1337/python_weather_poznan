#5/16/2021, first python script - web scrapping weather of my city
import requests
from bs4 import BeautifulSoup
page = requests.get("https://pogoda.interia.pl/prognoza-dlugoterminowa-poznan,cId,27457") #site to scrap weather data
soup = BeautifulSoup(page.content, 'html.parser')

def weather():
    temperature = soup.find('div', class_='weather-currently-temp-strict').get_text()
    weather = input("Choose weather language (PL/ENG): ").upper()
    if weather == str("PL"):
         print(f'W Poznaniu obecnie jest {temperature}')
    elif weather == str("ENG"):
        print(f'In Poznan currently is {temperature}')

try:
    weather()
except KeyboardInterrupt:
    print('\nOops!')
