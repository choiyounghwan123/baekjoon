# 단어 공부

import sys

word = sys.stdin.readline().rstrip().upper()
hash_map = dict()

for alphabet in word:
    hash_map[alphabet] = hash_map.get(alphabet,0) + 1

max_frequency = max(hash_map.values())

frequency_letters = [letter for letter,frequency in hash_map.items() if frequency == max_frequency]

if len(frequency_letters) == 1:
    print(frequency_letters[0])
else:
    print("?")