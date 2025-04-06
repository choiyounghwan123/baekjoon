# 1343. 폴리오미노

s = input()

s = s.replace("XXXX","AAAA")
s = s.replace("XX", "BB")

if 'X' in s:
    print(-1)
else:
    print(s)