# 위상정렬 알고리즘 

from collections import deque
import copy

n = int(input())
time = [0] * (n+1)  # 강의 시간 저장할 테이블
indegree = [0] * (n+1)  # 선입차수 저장할 리스트
graph = [[] for _ in range(n+1)]    # 각 노드에 연결된 간선 정보를 담을 리스트

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]   # 강의 시간 시간 테이블에 저장 
    for x in data[1:-1]:    # 처음 시작값과 마지막 데이터는 제외. 슬라이싱 활용.
        graph[x].append(i)
        indegree[i] += 1
        

def topology_sort():
    result = copy.deepcopy(time)    # 최종 시간 값을 더해서 담을 결과 리스트 
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1, n+1):
        print(result[i])
        
topology_sort()