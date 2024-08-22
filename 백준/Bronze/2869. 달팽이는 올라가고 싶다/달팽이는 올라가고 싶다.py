import math
import sys

A,B,V = map(int,sys.stdin.readline().split())

print(math.ceil((V-B) / (A-B)))

