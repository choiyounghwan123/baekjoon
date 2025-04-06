# 2864. 5와 6의 차이

A,B = map(str,input().split())
min_ = int(A.replace('6','5')) + int(B.replace('6','5'))
max_ = int(A.replace('5','6')) + int(B.replace('5','6'))
print(min_,max_)
