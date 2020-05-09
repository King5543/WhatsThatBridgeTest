import csv
from math import sin, cos, sqrt, atan2, radians

USERLOCATION = [30, 30]
if __name__ == '__main__':
    with open('whatsthatbridgedata.csv') as f:
        file_reader = csv.reader(f)

        ranking_list = []
        for i in file_reader:
            bridge_latitude = i[0]
            bridge_longitude = i[1]

            R = 6373.0
            # Radius of the Earth
            popularity_num = float(i[2])
            # daily traffic numbers

            user_lat = USERLOCATION[0]
            user_long = USERLOCATION[1]
            # user location information

            bridge_location = [bridge_latitude, bridge_longitude]
            bridge_lat = radians(float(bridge_location[0]))
            bridge_long = radians(float(bridge_location[1]))
            # bridge location

            distance_lat = bridge_lat - user_lat
            distance_long = bridge_long - user_long
            a = sin(distance_lat / 2) ** 2 + cos(user_lat) * cos(bridge_lat) * sin(distance_long / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            # calculates distance of bridges from user

            distance_to_user = float(R * c)
            ranking_info = [i[3], distance_to_user, popularity_num]
            # returns bridge name, distance from user, and daily use number
            ranking_list.append(ranking_info)

    ranking_list.sort(key=lambda ranking_list: ranking_list[1])
    print(ranking_list)
    f.close()
    top_five_list = ranking_list[:5]
    top_five_list.sort(key=lambda top_five_list: top_five_list[2])
