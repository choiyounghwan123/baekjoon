# 4375. 1

import sys

try:
    while True:
        n = int(sys.stdin.readline())
        answer = 1
        while answer % n != 0:
            answer = answer * 10 + 1
        print(len(str(answer)))
except:
    pass