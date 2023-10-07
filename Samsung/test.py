dx = [0,1,0,-1]
dy = [-1,0,1,0]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
state = [[False]*n for _ in range(n)]
now_x = now_y = n//2
direction = 0
zero = [[-2,0,0.02],[-1,-1,0.1],[-1,0,0.07],[-1,1,0.01],[0,-2,0.05],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[2,0,0.02],[0,-1,0.55]]
one = [[-1,-1,0.01], [-1,1,0.01], [0,-2,0.02], [0,-1,0.07],[0,1,0.07],[0,2,0.02],[1,-1,0.1],[1,1,0.1],[2,0,0.05],[1,0,0.55]]
two = [[-2,0,0.02], [-1,-1,0.01],[-1,0,0.07],[-1,1,0.1],[0,2,0.05],[1,-1,0.01], [1,0,0.07], [1,1,0.1],[2,0,0.02],[0,1,0.55]]
trd = [[-2,0,0.05],[-1,-1,0.1],[-1,1,0.1],[0,-2,0.02], [0,-1,0.07],[0,1,0.07],[0,2,0.02],[1,-1,0.01],[1,1,0.01],[-1,0,0.55]]
total = 0
#print()

def dust(x,y):
    global direction,n,total
    
    t = 0
    if direction == 0:
        narr = zero           
    elif direction == 1:
        narr = one 
    elif direction == 2:
        narr = two
    else:
        narr = trd
    origin = arr[x][y]
    for dx, dy, p in narr:
        if p ==0.55:
            tmp = origin 
        else:
            tmp = int(p*arr[x][y])
        
        if not (0 <= x+dx < n and 0 <= y+dy < n):
            t+=tmp
            
        else:
            arr[x+dx][y+dy] += tmp
        #print(tmp)
        origin-=tmp
    #print(origin)
    total+=t
    arr[x][y] = 0 
# index = 1
state[now_x][now_y] = True
while True:
    if not(0<=now_x<n and 0<= now_y<n):
        break
    #print(now_x,now_y,direction)
    # index+=1
    now_x,now_y = now_x + dx[direction],now_y + dy[direction]
    state[now_x][now_y] = True
    #먼지계산
    if arr[now_x][now_y] == 0:
        pass
    else:
        dust(now_x,now_y)
    nx, ny = now_x + dx[(direction+1)%4],now_y + dy[(direction+1)%4]
    if state[nx][ny] == False:
        direction=(direction + 1)%4
        
#     for i in range(n):
#         for j in range(n):
#             print(arr[i][j],end = "\t")
#         print()
#     print()
    
# for i in range(n):
#     for j in range(n):
#         print(state[i][j],end = "\t")
#     print()

print(total)
