# 2941. 크로아티아 알파벳

word = input().rstrip()

croatia_char = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for char in croatia_char:
    word = word.replace(char,"*")
print(len(word))