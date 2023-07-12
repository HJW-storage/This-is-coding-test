# N, M ,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 리스트로 입력받기
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬
first_max = data[n-1] # 가장 큰 수
second_max = data[n-2] # 두번째로 큰 수

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first_max
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second_max # 두 번쨰로 큰 수를 한번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답압 출력