# 단방향 도로, 다익스트라 알고리즘 사용

import heapq
INF = int(1e9)
n, m, c = map(int, input().split())
distance = [INF] * (n+1)
start = c 
city = [[] for _ in range(n+1)]
# print(city)

for _ in range(m):
    x, y, z = map(int ,input().split())
    city[x].append((y, z))
    
def solution(start):
    q = []
    heapq.heappush(q, (0, start))   # 시작하는 자기 자신의 위치는 비용 0이다. 
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:    # 이미 최단거리가 확정된 도시에 대해서는 추가 계산 안한다.
            continue
        
        for i in city[now]: # i는 (y, z)의 형태이다. i[0] : 노드, i[1] : 비용 이다.
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost   # 최소 비용으로 갱신.
                heapq.heappush(q, (cost, i[0]))
                

solution(start)

# 아래와 같이하면 .count 에서도 순차탐색 시간 소요 + for 문에서도 순차탐색이므로 
# 이를 for문 하나로 묶어서 작성하는 것이 시간을 조금이라도 줄이는 코드고 깔끔하다. 
# city_cnt, max_time = 0, -1
# city_cnt = (n+1) - distance.count(INF) - 1 # -1은 자기자신 비용 0인거 제외
# for t in distance:
#     if t != INF and t > max_time:
#         max_time = t

# 해당 내용을 반영해서 작성해본다. 
city_cnt, max_time = 0, 0
for d in distance:
    if d != INF:
        city_cnt += 1
        max_time = max(max_time, d)
print(city_cnt - 1, max_time)   # -1 : 본인 자기 도시는 빼준다. 
