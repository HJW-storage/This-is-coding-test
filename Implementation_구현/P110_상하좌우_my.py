n = int(input())
data = list(input().split())
# print(data)

# 현재 좌표(dx, dy)
dx = 1
dy = 1

for i in data:
    if i == 'L':
        if dy - 1 >= 1:
            dy = dy - 1
    elif i == 'R':
        if dy + 1 <= n:
            dy = dy + 1
    elif i == 'U':
        if dx - 1 >= 1:
            dx = dx - 1
    elif i == 'D':
        if dx + 1 <= n:
            dx = dx + 1

print("최종 목적지 : {} {}".format(dx, dy))