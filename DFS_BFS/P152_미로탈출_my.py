############################# 2023-09-27 ######################################
# BFS 풀이

from collections import deque

def bfs(grid):
    que = deque()
    que.append((0,0)) 
    visited[0][0] = True    # 초기 위치 방문처리
    
    #     서 북 동 남
    dr = [0, -1, 0, 1]  
    dc = [-1, 0, 1, 0]
    while que:
        cur_r, cur_c = que.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if next_r >= 0 and next_r < n and next_c >= 0 and next_c < m:
                if grid[next_r][next_c] == 1: # 갈 수 있는 곳이면
                    if not visited[next_r][next_c]: # 방문하지 않은 곳이면
                        que.append((next_r, next_c))
                        visited[next_r][next_c] = True  # 방문처리
                        grid[next_r][next_c] = grid[cur_r][cur_c] + 1
                        if next_r == n-1 and next_c == m-1:
                            print("목적지 도착 탈출")
                            # 반드시 미로를 탈출할 수 있는 형태로 제시된다고 했기에 해당 부분에서 return은 무조건 거친다.
                            return grid[n-1][m-1]  

# 입력
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))
    
# print(grid)
visited = [[False] * m for _ in range(n)]

# result = bfs(grid)
print("최소 이동 칸 개수는 : {}".format(bfs(grid)))
print(grid)


# # 방법 2 
# from collections import deque

# def bfs(grid):
#     que = deque()
#     que.append((0,0,1)) # 현재 위치 0,0 과 거리 1 (distance 정보도 같이 큐에)
#     visited[0][0] = True    # 초기 위치 방문처리
    
#     #     서 북 동 남
#     dr = [0, -1, 0, 1]  
#     dc = [-1, 0, 1, 0]
#     while que:
#         cur_r, cur_c, distance = que.popleft()
#         for i in range(4):
#             next_r = cur_r + dr[i]
#             next_c = cur_c + dc[i]
#             if next_r >= 0 and next_r < n and next_c >= 0 and next_c < m:
#                 if grid[next_r][next_c] == 1: # 갈 수 있는 곳이면
#                     if not visited[next_r][next_c]: # 방문하지 않은 곳이면
#                         que.append((next_r, next_c, distance + 1))
#                         visited[next_r][next_c] = True  # 방문처리
#                         if next_r == n-1 and next_c == m-1:
#                             print("목적지 도착 탈출")
#                             # 반드시 미로를 탈출할 수 있는 형태로 제시된다고 했기에 해당 부분에서 return은 무조건 거친다.
#                             return distance + 1   

# # 입력
# n, m = map(int, input().split())
# grid = []
# for _ in range(n):
#     grid.append(list(map(int, input())))
    
# # print(grid)
# visited = [[False] * m for _ in range(n)]

# # result = bfs(grid)
# print("최소 이동 칸 개수는 : {}".format(bfs(grid)))
# print(grid)