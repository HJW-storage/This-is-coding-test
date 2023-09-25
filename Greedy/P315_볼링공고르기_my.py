################### 2023-09-25 ###################
# 조합 이용. 
from itertools import combinations

n, m = map(int, input().split())
boling_balls = list(map(int, input().split()))

collect = list(combinations(boling_balls, 2))
result = len(collect)
for i in range(len(collect)):
    if collect[i][0] == collect[i][1]:
        result -= 1
        
print(result)