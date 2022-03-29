import sys
from math import sqrt, cos


def Distance(longitude_A, latitude_A, longitude_B, latitude_B):
    distance_x = (longitude_B - longitude_A) * cos((latitude_A + latitude_B) / 2)
    distance_y = latitude_B - latitude_A
    distance = sqrt((distance_x**2 + distance_y**2)) * 6371
    return distance


my_longitude = float(input().replace(",", "."))
my_latitude = float(input().replace(",", "."))
n = int(input())

location = ["", 100000000]
for _ in range(n):
    defib = input().split(";")
    longitude_B = float(defib[4].replace(",", "."))
    latitude_B = float(defib[5].replace(",", "."))
    distance = Distance(my_longitude, my_latitude, longitude_B, latitude_B)
    if distance < location[1]:
        location[0] = defib[1]
        location[1] = distance

print(location[0])
