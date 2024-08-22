# 집함

import sys

s = set()

for _ in range(int(sys.stdin.readline())):
    order = list(map(str,sys.stdin.readline().rstrip().split()))

    if order[0] == "add":
        s.add(int(order[1]))

    elif order[0] == "check":
        if int(order[1]) in s:
            print("1")
        else:
            print("0")

    elif order[0]== "remove":
        if int(order[1]) in s:
            s.discard(int(order[1]))
    elif order[0] == "toggle":
        if int(order[1]) in s:
            s.discard(int(order[1]))
        else:
            s.add(int(order[1]))
    elif order[0] == "all":
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    else:
        s.clear()