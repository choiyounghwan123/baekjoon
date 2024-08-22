# 좌표 정렬하기 2

import sys

coordinates = []

for _ in range(int(sys.stdin.readline())):
    coordinates.append(list(map(int,sys.stdin.readline().split())))

for coordinate in sorted(coordinates,key=lambda a:(a[1],a[0])):
    print(coordinate[0], coordinate[1])