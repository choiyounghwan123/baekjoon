import sys

for _ in range(int(sys.stdin.readline())):
    H,W,N = map(int,sys.stdin.readline().split())
    floor = N % H
    room_line = (N//H + 1)
    if floor == 0:
        floor = H
        room_line-= 1
    print(floor * 100 + room_line)

