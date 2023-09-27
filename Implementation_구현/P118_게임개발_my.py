n, m = map(int, input().split())
dx, dy, dd = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
print(arr)

d_dx = [-1, 0, 1, 0]
d_dy = [0, -1, 0, 1]


while True:
    end_condition = 0     # 메뉴얼 3번 동작을 위한 카운트
    for _ in range(4):  # 왼쪽 방향부터 4번 검사
        end_condition += 1
        dd -= 1
        if dd == -1:
            dd = 3      # 초기화
        next_row = dx + d_dx[dd]
        next_col = dy + d_dy[dd]
        if (next_row >= 0) and (next_row < n) and (next_col >= 0) and (next_col < m):
            if arr[next_row][next_col] == 0:
                arr[dx][dy] = 3     # 한번 지나간 곳은 3으로 표시
                dx, dy = next_row, next_col   # 이동하고 for문 탈출
                break

    if end_condition == 4:
        temp_direction = dd + 2
        if temp_direction >= 4:
            temp_direction -= 4
        next_row = dx + d_dx[temp_direction]
        next_col = dy + d_dy[temp_direction]
        if arr[next_row][next_col] == 1:    # 메뉴얼 3번 동작에서 뒤쪽 이동시 바다인 경우, 프로그램 종료
            break
        else:
            arr[dx][dy] = 3
            dx, dy = next_row, next_col
        # print(arr)
print(arr)

# 배열에서 3 개수 세기
count = 0
for i in range(n):
    count += arr[i].count(3)

print("최종 결과 : {}".format(count))