# 2745. 진법변환

N,B = map(str,input().split())
B = int(B.strip())
N = list(N)
result = 0
for i in range(len(N)-1,-1,-1):
    if N[i].isalpha():
        result += ((ord(N[i]) - 55)*(B ** (len(N)-1 - i)))
    else:
        result += int(N[i]) * (B ** (len(N)-1 - i))
print(result)