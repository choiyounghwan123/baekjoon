# 숫자 카드 2

import sys

card_dict = dict()
N = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))
for card in cards:
    card_dict[card] = card_dict.get(card,0) + 1

N = int(sys.stdin.readline())

result = list(map(int,sys.stdin.readline().split()))

for r in result:
    print(card_dict.get(r,0),end=" ")