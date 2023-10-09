# 양방향 도로이면서, 모든 비용은 1로 동일하다. 

start = 1
n, m = map(int, input().split())
INF = int(1e9)  # 무한대 값으로 10억을 정의
city = [[INF] * (n+1) for _ in range(n+1)]  # 2차원 리스트 

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 도로이면서, 모든 도로의 비용은 1이다.
    city[a][b] = 1
    city[b][a] = 1
# print(city)
    
x, k = map(int, input().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            city[a][b] = 0  # 자기자신에게 가는 비용은 0 

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            city[a][b] = min(city[a][b], city[a][k]+city[k][b])
            
# print(city)
if city[start][k] == INF or city[k][x] == INF:
    print("-1")
else:
    min_distance = city[start][k] + city[k][x]
    print(min_distance)

