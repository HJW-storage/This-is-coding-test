n, m = map(int, input().split())
dx, dy, dd = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
print(arr)

d_dx = [-1, 0, 1, 0]
d_dy = [0, -1, 0, 1]


while True:
    cnt = 0     # 메뉴얼 3번 동작을 위한 카운트
    for _ in range(4):  # 왼쪽 방향부터 4번 검사
        cnt += 1
        dd -= 1
        if dd == -1:
            dd = 3      # 초기화
        next_dx = dx + d_dx[dd]
        next_dy = dy + d_dy[dd]
        if (next_dx >= 0) and (next_dx < n) and (next_dy >= 0) and (next_dy < m):
            if arr[next_dx][next_dy] == 0:
                arr[dx][dy] = 3     # 한번 지나간 곳은 3으로 표시
                dx, dy = next_dx, next_dy   # 이동하고 for문 탈출
                break

    if cnt == 4:
        temp_d = dd + 2
        if temp_d >= 4:
            temp_d -= 4
        next_dx = dx + d_dx[temp_d]
        next_dy = dy + d_dy[temp_d]
        if arr[next_dx][next_dy] == 1:    # 메뉴얼 3번 동작에서 뒤쪽 이동시 바다인 경우, 프로그램 종료
            break
        else:
            arr[dx][dy] = 3
            dx, dy = next_dx, next_dy
        # print(arr)
print(arr)

# 배열에서 3 개수 세기
count = 0
for i in range(n):
    count += arr[i].count(3)

print("최종 결과 : {}".format(count))