import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    bridge_url = 'https://bridgehunter.com/ia/dubuque/4320/'
    bridge_specifics = requests.get(bridge_url).text
    # get request the HTML content
    soup = BeautifulSoup(bridge_specifics, 'html.parser')
    # parses through the html page text
    bridge_latitude_longitude_traffic = []
    bridge_latitude = float(soup.select('span.latitude')[0].text)
    bridge_longitude = float(soup.select('span.longitude')[0].text)
    bridge_traffic = float(soup.select('div.section dd')[10].text.replace(",", ''))
    bridge_latitude_longitude_traffic.append(bridge_latitude)
    bridge_latitude_longitude_traffic.append(bridge_longitude)
    bridge_latitude_longitude_traffic.append(bridge_traffic)
    print(bridge_latitude_longitude_traffic)
    # latitude, longitude, and traffic made into a list
