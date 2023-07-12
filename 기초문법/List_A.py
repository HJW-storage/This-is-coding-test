# 보통 컴퓨터 시스템은 수 데이터를 처리할 때 2진수를 이용
# 현대 컴퓨터 시스템은 대체로 실수 정보를 표현하는 정확도에 한계를 가진다.
fa = 0.3 + 0.6
print(fa)

if fa == 0.9:
    print(True)
else:
    print(False)

round_fa = round(fa, 4)
print(round_fa)

# 크기가 N인 1차원 리스트를 초기화
n = 10
list_a = [0] * n
print(list_a)

# List Comprehension
arr_1 = [i for i in range(20) if i % 2 == 1]
print(arr_1)

arr_2 = [i*i for i in range(1, 10)]
print(arr_2)

# 크기가 N(행) x M(열) 크기의 2차원 리스트 초기화
n1 = 3
m1 = 4
arr_nm = [[0] * m1 for _ in range(n1)] # 2차원 리스트 초기화는 리스트 컴프리헨션 방법을 꼭 사용해야한다.
# https://mingrammer.com/underscore-in-python/ 참고
print(arr_nm)
arr_nm[1][1] = 5
print(arr_nm)

# 특정한 값의 원소를 모두 제거하기
list_aa = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]
result_aa = [i for i in list_aa if i not in remove_set]
print(result_aa)
