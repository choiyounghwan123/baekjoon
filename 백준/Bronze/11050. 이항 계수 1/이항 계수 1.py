# 이항 계수 1
import math
import sys

N,K = map(int,sys.stdin.readline().split())

print(math.factorial(N) // (math.factorial(N-K)*math.factorial(K)))