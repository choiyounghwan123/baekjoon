# 3029. 경고

import datetime

a = datetime.datetime.strptime(input(), "%H:%M:%S")
b = datetime.datetime.strptime(input(), "%H:%M:%S")
if a == b:
    print("24:00:00")
    exit()
if a > b:
    b += datetime.timedelta(days=1)

result = str(b-a).split(":")

for i in range(len(result)):
    if len(result[i]) == 1:
        result[i] = result[i].zfill(2)

print(result[0]+":"+result[1]+":"+result[2])
