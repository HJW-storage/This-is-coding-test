# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# state = [[0]*n for _ in range(n)]
# now_x = now_y = n//2
# direction = 0
# zero = [[-2,0,0.02],[-1,-1,0.1],[-1,0,0.07],[-1,1,0.01],[0,-2,0.05],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[2,0,0.02],[0,-1,"A"]]
# one = [[-1,-1,0.01], [-1,1,0.01], [0,-2,0.02], [0,-1,0.07],[0,1,0.07],[0,2,0.02],[1,-1,0.1],[1,1,0.1],[2,0,0.05],[1,0,"A"]]
# two = [[-2,0,0.02], [-1,-1,0.01],[-1,0,0.07],[-1,1,0.1],[0,2,0.05],[1,-1,0.01], [1,0,0.07], [1,1,0.1],[2,0,0.02],[0,1,"A"]]
# trd = [[-2,0,0.05],[-1,-1,0.1],[-1,1,0.1],[0,-2,0.02], [0,-1,0.07],[0,1,0.07],[0,2,0.02],[1,-1,0.01],[1,1,0.01],[-1,0,"A"]]
# total = 0
# #print()
# def dust(x,y):
#     global direction,n,total
    
#     t = 0
#     if direction == 0:
#         narr = zero           
#     elif direction == 1:
#         narr = one 
#     elif direction == 2:
#         narr = two
#     else:
#         narr = trd
#     origin = arr[x][y]
#     for dx, dy, p in narr:
#         if p =="A":
#             tmp = origin 
#         else:
#             tmp = int(p*arr[x][y])
        
#         if not (0 <= x+dx < n and 0 <= y+dy < n):
#             t+=tmp
            
#         else:
#             arr[x+dx][y+dy] += tmp
#         #print(tmp)
#         origin-=tmp
#     #print(origin)
#     total+=t
#     arr[x][y] = 0 
# index = 1
# while True:
#     if not(0<=now_x<n and 0<= now_y<n):
#         break
#     #print(now_x,now_y,direction)
#     state[now_x][now_y] = index
#     index+=1
#     now_x,now_y = now_x + dx[direction],now_y + dy[direction]
#     #먼지계산
#     if arr[now_x][now_y] == 0:
#         pass
#     else:
#         dust(now_x,now_y)
#     nx, ny = now_x + dx[(direction+1)%4],now_y + dy[(direction+1)%4]
#     if state[nx][ny] == 0:
#         direction=(direction + 1)%4
        
# #     for i in range(n):
# #         for j in range(n):
# #             print(arr[i][j],end = "\t")
# #         print()
# #     print()
    
# # for i in range(n):
# #     for j in range(n):
# #         print(state[i][j],end = "\t")
# #     print()

# print(total)



############################## 2023-10-06 ################################
# https://www.acmicpc.net/problem/20057

n = int(input())
sand = []
for _ in range(n):
    sand.append(list(map(int, input().split())))

# print(sand)
cur_row, cur_col = n//2, n//2   # 시작 위치
out_sand = 0    # 밖으로 나가는 모래. 구해야 하는 것. 
direction = 0   # 방향

move_left = [[-2, 0, 0.02], [-1, -1, 0.1], [-1, 0, 0.07], [-1, 1, 0.01], [0, -2, 0.05],
            [1, -1, 0.1], [1, 0, 0.07], [1, 1, 0.01], [2, 0, 0.02], [0, -1, "A"]]
move_down = [[0, -2, 0.02], [-1, -1, 0.01], [0, -1, 0.07], [1, -1, 0.1], [2, 0, 0.05],
            [-1, 1, 0.01], [0, 1, 0.07], [1, 1, 0.1], [0, 2, 0.02], [1, 0, "A"]]
move_right = [[2, 0, 0.02], [1, 1, 0.1], [1, 0, 0.07], [1, -1, 0.01], [0, 2, 0.05],
            [-1, 1, 0.1], [-1, 0, 0.07], [-1, 1, 0.01], [-2, 0, 0.02], [0, 1, "A"]]
move_up = [[0, 2, 0.02], [1, 1, 0.01], [0, 1, 0.07], [-1, 1, 0.1], [-2, 0, 0.05],
            [1, -1, 0.01], [0, -1, 0.07], [-1, -1, 0.1], [0, -2, 0.02], [-1, 0, "A"]]

def move_tonado(x, y):
    global direction, out_sand
    
    move_plan = []
    if direction == 0:
        move_plan = move_left
    elif direction == 1:
        move_plan = move_down
    elif direction == 2:
        move_plan = move_right
    else:
        move_plan = move_up
    
    # print(move_plan)
    origin = sand[x][y]
    t = 0
    for row, col, mux in move_plan:
        next_x = x + row
        next_y = y + col
        if mux == "A":
            tmp = origin
        else:
            tmp = int(mux*sand[x][y])
        
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
            sand[next_x][next_y] += tmp
        else:
            t += tmp   # 밖으로 나가는 모래
        origin -= tmp
        
    out_sand += t
    sand[x][y] = 0
    # print(out_sand)
    # print(sand)
    
visited = [[False] * n for _ in range(n)]
visited[cur_row][cur_col] = True
dx = [ 0, 1, 0, -1]
dy = [-1, 0, 1,  0]
# cal_cnt = 0
while True:
    if not(0<=cur_row<n and 0<= cur_col<n):
        break
    
    visited[cur_row][cur_col] = True  # 방문
    
    cur_row = cur_row + dx[direction] # 이동
    cur_col = cur_col + dy[direction] # 이동
    
    if sand[cur_row][cur_col] == 0:
        pass
    else:
        move_tonado(cur_row, cur_col)
        # print("토네이도 이동")
        
    next_row = cur_row + dx[(direction + 1) % 4]
    next_col = cur_col + dy[(direction + 1) % 4]
    if visited[next_row][next_col] == False:
        direction = (direction + 1) % 4    
    
    # cal_cnt += 1
# print("결과 : {}".format(out_sand))
print(out_sand)
