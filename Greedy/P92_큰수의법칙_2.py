# 해당 문제에서 M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다.
# 수학적 아이디어를 고려하여 간단하게 구현할 수 있다.  (p.94 참고)

# N, M ,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 리스트로 입력받기
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬
first_max = data[n-1] # 가장 큰 수
second_max = data[n-2] # 두번째로 큰 수

# 가장 큰 수가 더해지슷 횟수 계산
count = (m // (k+1)) * k
count += (m % (k+1))

result = 0
result += count * first_max # 가장 큰 수 더하기
result += (m - count) * second_max # 가장 큰 수 더하기

print(result) # 최종 답안 출력