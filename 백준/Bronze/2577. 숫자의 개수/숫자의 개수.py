import sys
num = 1
for _ in range(3):
    num *= int(sys.stdin.readline())

res = [0]*10

for i in list(str(num)):
    res[int(i)]+=1

for i in res:
    print(i)
