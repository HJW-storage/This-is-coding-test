############################# 2023-09-27 ######################################
# DFS 풀이
# def dfs(r, c):
#     visited[r][c] = True    # 방문처리
#     #     서 북 동 남
#     dr = [0, -1, 0, 1]  
#     dc = [-1, 0, 1, 0]
    
#     for i in range(4):
#         next_r = r + dr[i]
#         next_c = c + dc[i]
#         if next_r >= 0 and next_r < n and next_c >= 0 and next_c < m:
#             if grid[next_r][next_c] == 0: # 갈 수 있는 곳이면
#                 if not visited[next_r][next_c]: # 방문하지 않은 곳이면
#                     dfs(next_r, next_c) # 재귀함수 호출

# # 입력 
# n, m = map(int, input().split())
# grid = []
# for _ in range(n):
#     grid.append(list(map(int, input())))
    

# visited = [[False] * m for _ in range(n)]   # 방문처리할 2차원 리스트 초기화

# result = 0
# for i in range(n):
#     for j in range(m):
#         if grid[i][j] == 0 and visited[i][j] == False:
#             dfs(i, j)
#             result += 1
            
# print("아이스크림 개수 : {}".format(result))


# BFS 풀이
from collections import deque
def bfs(r, c):
    que = deque()
    que.append((r, c))
    visited[r][c] = True    # 초기 위치 방문처리
    
    #     서 북 동 남
    dr = [0, -1, 0, 1]  
    dc = [-1, 0, 1, 0]
    
    while que:
        cur_r, cur_c = que.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if next_r >= 0 and next_r < n and next_c >= 0 and next_c < m:
                if grid[next_r][next_c] == 0: # 갈 수 있는 곳이면
                    if not visited[next_r][next_c]: # 방문하지 않은 곳이면
                        que.append((next_r, next_c))
                        visited[next_r][next_c] = True  # 방문처리
# 입력 
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]   # 방문처리할 2차원 리스트 초기화

result = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and visited[i][j] == False:
            bfs(i, j)
            result += 1
            
print("아이스크림 개수 : {}".format(result))