############################### 2023-10-03 ###################################
from collections import deque

# BFS의 총 시간복잡도 O(M + N)
def bfs():
    que = deque()
    que.append(x)
    
    # 시간복잡도 O(M)
    while que:
        now = que.popleft()
        for next_city in graph[now]:
            if distance[next_city] == -1:
                que.append(next_city)
                distance[next_city] = distance[now] + 1
    
    # print(distance)
    flag = False
    # 시간복잡도 O(N)
    for i in range(n+1):
        if distance[i] == k:
            print(i)
            flag = True
            
    if flag == False:
        print(-1)
    
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
# print(graph)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
# print(graph)
distance = [-1] * (n+1)
distance[x] = 0
# print(distance)

bfs()