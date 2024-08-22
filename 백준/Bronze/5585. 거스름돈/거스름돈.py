# 거스름돈

import sys

coins = [500,100,50,10,5,1]
count = 0
price = 1000-int(sys.stdin.readline())

for coin in coins:
    count += price//coin
    price %= coin

print(count)