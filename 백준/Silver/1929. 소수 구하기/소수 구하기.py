# 소수 구하기

import math
import sys
# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

M,N = map(int,sys.stdin.readline().split())

for i in range(M,N+1):
    if is_prime_number(i):
        print(i)