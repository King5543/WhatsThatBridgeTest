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
    if '+' in bridge_latitude:
        bridge_latitude.replace('+', '')
        bridge_latitude = int(bridge_latitude)
    else:
        bridge_latitude = int(bridge_latitude)

    if '+' in bridge_longitude:
        bridge_longitude.replace('+', '')
        bridge_longitude = int(bridge_longitude)
    else:
        bridge_longitude = int(bridge_longitude)
    bridge_location.append(bridge_latitude)
    bridge_location.append(bridge_longitude)
    print(bridge_location)
