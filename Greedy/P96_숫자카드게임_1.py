# min() 함수를 이용한 답안 예시
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)   # 현재 줄에서 가장 작은 수 찾기
    result = max(result, min_value)     # '가장 작은 수'들 중에서 가장 큰 수 찾기

print("최종 결과 : {}".format(result))


# 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001   # 문제 조건에서 입력되는 수는 <= 10000 이라고 했으므로

    # 현재 줄에서 가장 작은 수 찾기
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)     # '가장 작은 수'들 중에서 가장 큰 수 찾기

print("최종 결과 : {}".format(result))