# 곱셈

A = int(input())
B = list(input())

for num in reversed(B):
    print(A*int(num))
print(A*int("".join(B)))
