# P.512
n, m = map(int, input().split())
boling_balls = list(map(int, input().split()))

boling_balls_cnt = [0] * (m+1)
for x in boling_balls:
    boling_balls_cnt[x] += 1
    
# print(boling_balls_cnt)

result = 0
for i in range(1, m):
    n -= boling_balls_cnt[i]
    result += boling_balls_cnt[i] * n
    
print(result)