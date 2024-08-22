# Four Squares

import sys

N = int(sys.stdin.readline())

arr = [0 if i**0.5%1 else 1 for i in range(N+1)]

if arr[N]:
    print("1")
else:
    min_ = 4
    for i in range(int(N ** 0.5),0,-1):
        if arr[N-i**2]:
            min_ = 2
            break
        else:
            for j in range(int((N - i ** 2) ** 0.5), 0, -1):
                if arr[(N - i ** 2) - j ** 2]:  # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                    min_ = 3

    print(min_)

