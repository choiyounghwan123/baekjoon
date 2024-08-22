import sys

sets = set()

for _ in range(10):
    sets.add(int(sys.stdin.readline())%42)
print(len(sets))