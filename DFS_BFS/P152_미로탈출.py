from collections import deque

# 탐색 알고리즘 bfs 구현하기
def bfs(x, y):
    que = deque()
    que.append((x, y))
    # 큐가 빌때까지 반복
    while que:
        x, y = que.popleft()
        # 현재 위치에서 4가지 방향으로의 위치를 확인한다.
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리를 기록.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리를 반환한다.
    return graph[n-1][m-1]
    
# 행, 열 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
# 이동할 네가지 방향 정의 - 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력.
print(bfs(0, 0))

