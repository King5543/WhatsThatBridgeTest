from math import sin, cos, sqrt, atan2, radians

if __name__ == '__main__':
    bridge_distances = []
    R = 6373.0
    # Radius of the Earth
    base_location = [50, 50, "Doesn't matter", "name"]
    base_lat = base_location[0]
    base_long = base_location[1]
    # user location
    new_location = [30, 30, "Doesn't matter", "name"]
    new_lat = radians(new_location[0])
    new_long = radians(new_location[1])
    # bridge location
    distance_lat = new_lat - base_lat
    distance_long = new_long - base_long
    a = sin(distance_lat/2)**2 + cos(base_lat)*cos(new_lat)*sin(distance_long/2)**2
    c = 2* atan2(sqrt(a), sqrt(1-a))
    distance = float(R*c)
    bridge_distances.append({new_location[3]: distance})
    # calculates distance of bridges from user
    print(bridge_distances)
