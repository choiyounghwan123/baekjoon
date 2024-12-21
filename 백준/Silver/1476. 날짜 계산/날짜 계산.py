# 1476. 날짜 계산

E,S,M = map(int,input().split())

e,s,m = 1,1,1
day = 1
while True:
    if e == E and s == S and m == M:
        print(day)
        break
    if e+1 == 16:
        e = 1
    else:
        e+=1
    if s + 1 == 29:
        s = 1
    else:
        s+=1
    if m + 1 == 20:
        m = 1
    else:
        m+=1
    day+=1
