# 9046. 복호화

T = int(input())

import collections

for _ in range(T):
    cryptogram = input().replace(" ","")
    counter = collections.Counter(cryptogram)
    a = counter.most_common(2)
    if a and len(a) >1 and a[0][1] == a[1][1]:
        print("?")
    else:
        print(a[0][0])
