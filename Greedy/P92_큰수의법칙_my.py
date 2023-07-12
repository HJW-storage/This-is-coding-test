import time
# start_time = time.time()

# N, M, K 입력 받기
N, M, K = map(int, input().split())  # 정수형으로
# 1차원 배열 입력받기 = 정수형 리스트로 저장
num_list = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3]

max_value = max(num_list)

cnt_max = num_list.count(max_value)
# print(cnt_max)

max_result = 0
if cnt_max == 1:
    num_list.remove(max_value) # 최대값 제외한 리스트 만들고
    # print(num_list)
    max_value_1 = max(num_list) # 두번쨰로 큰 수 찾기
    # print(max_value_1)
    cnt = 0
    for i in range(M):
        cnt += 1
        if cnt == K+1:
            cnt = 0
            max_result += max_value_1
        else:
            max_result += max_value
else:
    max_result = max_value * M

print(max_result)

# 함수로 만들어서 표현하면 다음과 같다
# def Find_maxsum(cnt_max, M, K):
#     max_result = 0
#     if cnt_max == 1:
#         num_list.remove(max_value)
#         # print(num_list)
#         max_value_1 = max(num_list)
#         # print(max_value_1)
#         cnt = 0
#         for i in range(M):
#             cnt += 1
#             if cnt == K + 1:
#                 cnt = 0
#                 max_result += max_value_1
#             else:
#                 max_result += max_value
#     else:
#         max_result = max_value * M
#
#     print(max_result)
# # N, M, K 입력 받기
# N, M, K = map(int, input().split())  # 정수형으로
#
# # 1차원 배열 입력받기 = 정수형 리스트로 저장
# num_list = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3]
#
# # start_time = time.time()
#
# max_value = max(num_list)
#
# cnt_max = num_list.count(max_value)
#
# Find_maxsum(cnt_max, M, K)