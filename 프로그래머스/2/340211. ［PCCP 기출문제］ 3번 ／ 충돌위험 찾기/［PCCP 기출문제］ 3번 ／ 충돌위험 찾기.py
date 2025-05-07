# PCCP 3. 충돌위험 찾기
from collections import Counter, defaultdict

def solution(points, routes):
    routeList = defaultdict(list)
    for route in routes:
        j = 1
        routeList[j].append((tuple(points[route[0]-1])))
        j+=1
        for i in range(1,len(route)):
            start_x,start_y = points[route[i-1]-1]
            target_x,target_y = points[route[i]-1]
            while start_x != target_x:
                if start_x > target_x:
                    start_x-=1
                elif start_x < target_x:
                    start_x+=1
                routeList[j].append((start_x, start_y))
                j += 1


            while start_y != target_y:
                if start_y > target_y:
                    start_y-=1
                elif start_y < target_y:
                    start_y+=1
                routeList[j].append((start_x, start_y))
                j+=1

    result = 0
    for key in routeList:
        c = Counter(routeList[key])
        for k,c in c.items():
            if c>1:
                result+=1
    return result

print(solution( [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))