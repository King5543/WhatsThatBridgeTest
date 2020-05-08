import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    bridge_start_url = 'https://bridgehunter.com/category/status/open/'
    # keeps url
    bridge_content = requests.get(bridge_start_url).text
    # get request the HTML content
    soup = BeautifulSoup(bridge_content, 'html.parser')
    # parses through the html page text
    link_bridges = soup.select('div.x a.name')
    print(link_bridges)
    # finds all bridge names and url pairs for each bridge
    page = 1
    bridge_list = []
    bridge = 0
    while bridge < len(link_bridges):
        href = link_bridges[bridge].get('href')
        name_bridge = link_bridges[bridge].get_text()
        new_bridge = [name_bridge, href]
        bridge_list.append(new_bridge)
        bridge += 1
        # makes list with bridge name and it's url
    # bridge_list is filled with all the bridges on this page and their urls
    print(bridge_list[0][1])

    """while page <= 228:
        bridge_page_url = 'https://bridgehunter.com/category/status/open/page' + str(page) + '/'
        bridge_content = requests.get(bridge_start_url).text
        # get request the HTML content
        soup = BeautifulSoup(bridge_content, 'html.parser')
        # parses through the html page text
        link_bridges = soup.select('div.x a.name')
        print('Made it through a page')
        # finds all bridge names and url pairs for each bridge
        bridge = 0
        while bridge < len(link_bridges):
            href = link_bridges[bridge].get('href')
            name_bridge = link_bridges[bridge].get_text()
            new_bridge = [name_bridge, href]
            bridge_list.append(new_bridge)
            bridge += 1
            # makes list with bridge name and it's url
        # bridge_list is filled with all the bridges on this page and their urls
        print("another bridge down")
        page += 1
    print('We done did it!')"""
    # gets the name and link for every bridge
    bridge_info = 0
    while bridge_info < len(bridge_list):
        bridge_page = bridge_list[bridge_info][1]
        bridge_url = 'https://bridgehunter.com' + bridge_page
        bridge_specifics = requests.get(bridge_url).text
        # get request the HTML content
        soup = BeautifulSoup(bridge_specifics, 'html.parser')
        # parses through the html page text
        bridge_latitude_longitude_traffic_name = []
        bridge_latitude = float(soup.select('span.latitude')[0].text)
        bridge_longitude = float(soup.select('span.longitude')[0].text)

        try:
            bridge_traffic = float(soup.select('div.section dd')[10].text.replace(",", ''))
            bridge_latitude_longitude_traffic_name.append(bridge_latitude)
            bridge_latitude_longitude_traffic_name.append(bridge_longitude)
            bridge_latitude_longitude_traffic_name.append(bridge_traffic)
            bridge_latitude_longitude_traffic_name.append(bridge_list[bridge_info][0])
            print(bridge_latitude_longitude_traffic_name)
            # latitude, longitude, and traffic made into a list
            bridge_info += 1

        except:
            bridge_traffic = 0
            bridge_latitude_longitude_traffic_name.append(bridge_latitude)
            bridge_latitude_longitude_traffic_name.append(bridge_longitude)
            bridge_latitude_longitude_traffic_name.append(bridge_traffic)
            bridge_latitude_longitude_traffic_name.append(bridge_list[bridge_info][0])
            print(bridge_latitude_longitude_traffic_name)
            # latitude, longitude, and traffic made into a list
            bridge_info += 1
