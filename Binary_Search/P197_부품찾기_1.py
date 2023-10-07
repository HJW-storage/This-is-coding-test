# # 계수정렬 개념을 이용한 풀이
# n = int(input())

# arr = [0] * 1000001
# parts = list(map(int, input().split()))
# for i in parts:
#     arr[i] = 1
    
# m = int(input())
# ask_parts = list(map(int, input().split()))

# for i in ask_parts:
#     if arr[i] == 1:
#         print("yes", end = ' ')
#     else:
#         print("no", end = ' ')

# 집합 자료형을 이용한 풀이
n = int(input())
parts = set(map(int, input().split()))  # 집합자료형

m = int(input())
ask_parts = list(map(int, input().split()))

for i in ask_parts:
    if i in parts:  # 집합자료형은 해시테이블을 이용하므로 탐색 시간복잡도 O(1)이다. 
        print("yes", end = ' ')
    else:
        print("no", end = ' ')

