############################### 2023-10-03 ###################################
####### 내 풀이 ####### 
from itertools import combinations  # 조합
from collections import deque   # 큐 
import copy # 깊은 복사. 
# https://wikidocs.net/16038  얕은 복사, 깊은 복사

def bfs(tmp_grid):
    # start_x, start_y = two_idx[0] # 0, 0
    # print(start_x, start_y)
    visited = [[False] * m for _ in range(n)]
    que = deque()
    # que.append((start_x, start_y))
    
    ## 시작점만 넣으면 안되는 경우가 생긴다. 답에서 요구하는 최대 개수보다 많을때가 생긴다.
    # 예를 들어 구석 2 주변으로 모든 벽이 둘러쌓였을 경우에, 다른 2에서 탐색을 안하니 정답보다 3이 더 큰 수가 출력된다.
    # 그래서 모든 2를 처음에 큐에 넣고 탐색해야한다. 
    for i in range(len(two_idx)):
        que.append(two_idx[i])
    # visited[start_x][start_y] = True
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    
    while que:
        cur_row, cur_col = que.popleft()
        for i in range(4):
            next_row = cur_row + dr[i]
            next_col = cur_col + dc[i]
            if next_row >= 0 and next_row < n and next_col >= 0 and next_col < m:
                if tmp_grid[next_row][next_col] == 0:
                    if visited[next_row][next_col] == False:
                        visited[next_row][next_col] = True
                        tmp_grid[next_row][next_col] = 2
                        que.append((next_row, next_col))
    
    # print(grid)                  
    cnt = 0                  
    for i in range(n):
        for j in range(m):
            if tmp_grid[i][j] == 0:
                cnt += 1
    # print(cnt)            
    safetyarea_cnt.append(cnt)

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0 
# 0 1 0 0 0 0 0
n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
    
# print(grid)

safetyarea_cnt = []

zero_idx, two_idx = [], []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            zero_idx.append((i, j))
        elif grid[i][j] == 2:
            two_idx.append((i, j))
            
# print(zero_idx)
three_combo = list(combinations(zero_idx, 3))    # 조합 이용. 0인 위치 3개 뽑기
# print(three_combo[0])

for i in range(len(three_combo)):
    tmp_grid = copy.deepcopy(grid)  # 깊은 복사. 
    for j in range(len(three_combo[i])):
        x, y = three_combo[i][j]
        tmp_grid[x][y] = 1
    # print(grid)
    bfs(tmp_grid)
    
# print(safetyarea_cnt)
print(max(safetyarea_cnt))