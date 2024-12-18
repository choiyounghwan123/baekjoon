# 10808. 알파벳 개수

s = input()
alphabets = [0] * 26

for char in s:
    alphabets[ord(char) - 97] += 1

for alphabet in alphabets:
    print(alphabet, end=" ")