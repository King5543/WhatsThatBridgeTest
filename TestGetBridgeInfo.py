import requests
import csv
from math import sin, cos, sqrt, atan2, radians
from bs4 import BeautifulSoup

USER_LOCATION = [50, 50, 'some', 'AUSTINTEST']


# test user location data


def distance_calc(base_location, new_location):
    R = 6373.0
    # Radius of the Earth
    popularity_num = new_location[2]
    # daily traffic numbers

    user_location = base_location
    user_lat = user_location[0]
    user_long = user_location[1]
    # user location information

    bridge_location = new_location
    bridge_lat = radians(bridge_location[0])
    bridge_long = radians(bridge_location[1])
    # bridge location

    distance_lat = bridge_lat - user_lat
    distance_long = bridge_long - user_long
    a = sin(distance_lat / 2) ** 2 + cos(user_lat) * cos(bridge_lat) * sin(distance_long / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    # calculates distance of bridges from user

    distance_to_user = float(R * c)
    return [bridge_location[3], distance_to_user, popularity_num]
    # returns bridge name, distance from user, and daily use number


if __name__ == '__main__':
    bridge_start_url = 'https://bridgehunter.com/category/status/open/'
    # keeps url

    bridge_content = requests.get(bridge_start_url).text
    # get request the HTML content

    soup = BeautifulSoup(bridge_content, 'html.parser')
    # parses through the html page text

    link_bridges = soup.select('div.x a.name')
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

    while page <= 228:
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

        page += 1
    print('We done did it!')
    # gets the name and link for every bridge

    bridge_info = 0
    bridge_info_list = []
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

            # latitude, longitude, traffic, and name made into a list
            # bridge_info_list.append(distance_calc(USER_LOCATION, bridge_latitude_longitude_traffic_name))
            bridge_info_list.append(bridge_latitude_longitude_traffic_name)
            bridge_info += 1

        except:
            bridge_traffic = 0
            bridge_latitude_longitude_traffic_name.append(bridge_latitude)
            bridge_latitude_longitude_traffic_name.append(bridge_longitude)
            bridge_latitude_longitude_traffic_name.append(bridge_traffic)
            bridge_latitude_longitude_traffic_name.append(bridge_list[bridge_info][0])
            # latitude, longitude, traffic, and name made into a list

            # distance = distance_calc(USER_LOCATION, bridge_latitude_longitude_traffic_name)
            # will need to alter^ so data is taken from database for calculation
            bridge_info_list.append(bridge_latitude_longitude_traffic_name)
            bridge_info += 1

    # bridge_info_list.sort(key=lambda bridge_info_list: bridge_info_list[1])
    # print(bridge_info_list)
    # top_five_closest_bridges = bridge_info_list[:5]
    # print(top_five_closest_bridges)
    # top_five_closest_bridges.sort(key=lambda top_five_closest_bridges: top_five_closest_bridges[2], reverse=True)
    # print(top_five_closest_bridges)
    file = open('whatsthatbridgedata.csv', 'w', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(bridge_info_list)
