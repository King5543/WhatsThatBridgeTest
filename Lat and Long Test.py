import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    bridge_url = 'https://bridgehunter.com/ia/dubuque/4320/'
    bridge_specifics = requests.get(bridge_url).text
    # get request the HTML content
    soup = BeautifulSoup(bridge_specifics, 'html.parser')
    # parses through the html page text
    bridge_location = []
    bridge_latitude = soup.select('span.latitude')[0].text
    bridge_longitude = soup.select('span.longitude')[0].text
    bridge_latitude = float(bridge_latitude)
    bridge_longitude = float(bridge_longitude)
    bridge_location.append(bridge_latitude)
    bridge_location.append(bridge_longitude)
    print(bridge_location)
    # latitude and longitude made into a list
