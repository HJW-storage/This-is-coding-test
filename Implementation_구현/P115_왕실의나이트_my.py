pos = list(input())
# l_pos = list(pos)
print(pos)

str_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
cnt = 1
for i in str_1:
    if pos[0] == i:
        pos[0] = cnt
    else:
        cnt += 1

pos[1] = int(pos[1])
print(pos)
dx, dy = pos[0], pos[1]

dx_h = [1, -1]
dy_h = [2, -2]
dx_v = [2, -2]
dy_v = [1, -1]

result = 0
for i in dx_h:
    for j in dy_h:
        if ((dx + i <= 8) and (dx + i >= 1)) and ((dy + j <= 8) and (dy + j >= 1)):
            result += 1

for i in dx_v:
    for j in dy_v:
        if ((dx + i <= 8) and (dx + i >= 1)) and ((dy + j <= 8) and (dy + j >= 1)):
            result += 1

print("최종 결과 : {}".format(result))


