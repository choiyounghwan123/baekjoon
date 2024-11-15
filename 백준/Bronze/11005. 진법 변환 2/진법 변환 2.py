# 진법 변환 2

N,B = map(int,input().split())
number_to_char = {i: chr(i + 55) if i >= 10 else str(i) for i in range(36)}

result = []

while N != 0:
    a,b = divmod(N,B)
    result.append(b)
    N = a

for i in range(len(result)):
    result[i] = number_to_char[result[i]]
result.reverse()
print("".join(result))