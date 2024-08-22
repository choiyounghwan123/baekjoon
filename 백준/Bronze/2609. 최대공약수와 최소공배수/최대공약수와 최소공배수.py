import sys

n1,n2 = map(int,sys.stdin.readline().split())
result = 1
for i in range(1,min(n1,n2)+1):
    if n1%i == 0 and n2%i == 0:
        result = i
print(result)

i = 1
while True:
    if (min(n1,n2)*i) % max(n1,n2) == 0:
        print(min(n1,n2)*i)
        break
    else:
        i+=1