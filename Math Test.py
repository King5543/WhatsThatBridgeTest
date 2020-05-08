from math import sin, cos, sqrt, atan2, radians

if __name__ == '__main__':
    bridge_distances = []
    R = 6373.0
    # Radius of the Earth

    user_location = [50, 50, "Doesn't matter", "name"]
    user_lat = user_location[0]
    user_long = user_location[1]
    # user location information

    bridge_location = [30, 30, "Doesn't matter", "name"]
    bridge_lat = radians(bridge_location[0])
    bridge_long = radians(bridge_location[1])
    # bridge location

    distance_lat = bridge_lat - user_lat
    distance_long = bridge_long - user_long
    a = sin(distance_lat/2)**2 + cos(user_lat)*cos(bridge_lat)*sin(distance_long/2)**2
    c = 2* atan2(sqrt(a), sqrt(1-a))

    distance = float(R*c)
    bridge_distances.append({bridge_location[3]: distance})
    # calculates distance of bridges from user

    print(bridge_distances)
