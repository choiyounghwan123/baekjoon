# 좌표 정렬하기

import sys

coordinate = []

for _ in range(int(sys.stdin.readline())):
    coordinate.append(list(map(int,sys.stdin.readline().split())))

for i in sorted(coordinate,key=lambda j:(j[0],j[1])):
    print(i[0], i[1])