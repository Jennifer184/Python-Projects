# tell_me_the_weather.py 
#   - Main entry point to WeatherApp.
#     This program reads the weather out loud.
#     A script that displays via command line 
#     and reads out loud the current temperature of a 
#     city that the user specifies. This uses 
#     google search and google text to speach.

# Requirements: 
#   OS: Windows
#   pip install BeautifulSoup4
#   pip install gtts

# To Run:
#   Use Windows PowerShell
#   $ python tell_me_the_weather.py

import re
import google_search
import text_to_talk
import current_time
import weather_map
import subprocess

def find_users_city():
    city = input('Enter the name of the city and country'
        +' you would like to look up: ')
    return city 

def get_city_temp(html):
    tempuatureStr = ''
    try:
        tempuatureStr = html.find('div', class_='BNeawe iBp4i AP7Wnd').text
    except Exception:
        print('tell_me_the_weather.py : line 29, Could not locate city temperature ')
        exit()
    return tempuatureStr

def get_city_name(html):
    city = ''
    try:
        city = html.find('div', attrs={'class':'Gx5Zad xpd EtOod pkphOe'}).find('span').text
    except Exception:
        print('tell_me_the_weather.py : line 38, Could not locate user\'s city ')
        exit()
    return city

# Not used
def get_temp_val_only(tempuatureStr):   
    regex = re.compile('([0-9]+)')
    tempVal = regex.match(tempuatureStr).group(0)
    return int(tempVal)

def capitalize_first_letter(city):
    return city[:0] + city[0].capitalize() + city[0 + 1:]

def search_for_city():
    usersCity = find_users_city()
    search = 'weather in ' + usersCity
    html = google_search.googleSearch(search)
    return html

def search_city_temp(html):
    city = get_city_name(html)
    tempuatureStr = get_city_temp(html)
    newCity = capitalize_first_letter(city)
    result = 'The temperature in ' + newCity + ' is currently ' + tempuatureStr 
    return result
  
def main():
    print('~ Weather Lookup ~ ')
    
    html = search_for_city()
    result = search_city_temp(html)
    #weather_map.get_weather_map()
    
    print(result)
    text_to_talk.speak(result)
    
if __name__ == '__main__':
    main()