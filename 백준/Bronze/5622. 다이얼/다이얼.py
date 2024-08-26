# 다이얼

import sys

numbers = list(sys.stdin.readline().rstrip())
result = 0

for number in numbers:
    if number in["A","B","C"]:
        result += 3
    elif number in "DEF":
        result += 4
    elif number in "GHI":
        result+=5
    elif number in "JKL":
        result += 6
    elif number in "MNO":
        result += 7
    elif number in "PQRS":
        result += 8
    elif number in "TUV" :
        result += 9
    elif number in "WXYZ":
        result += 10
    else:
        result += 11

print(result)