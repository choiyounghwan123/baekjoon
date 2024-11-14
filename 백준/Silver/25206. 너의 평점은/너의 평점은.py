# 25206. 너의 평점은

hash_map = {
    "A+" : 4.5,
    "A0": 4.0, "B+":3.5,"B0": 3.0,
    "C+":2.5, "C0":2.0,"D+":1.5,
    "D0":1.0,"F":0.0,"P":0
}

score = 0
total = 0
for _ in range(20):
    a,b,c = map(str,input().rstrip().split())
    score += float(b) * hash_map[c]
    if c != "P":
        total += float(b)
print(round(score/total,6))
