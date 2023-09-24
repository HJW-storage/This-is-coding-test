# n = int(input())
# data = list(map(int, input().split()))
# data.sort()     # 오름차순으로 정렬

# idx_len = len(data) - 1     # 인덱스로 접근하기 위해서 -1을 해준다.
# cnt_group = 0
# break_num = 0
# while True:
#     bound_line = idx_len    # 기준점으로 사용
#     idx_len -= data[idx_len]    # 오름차순 정렬을 기준으로 가장 큰 값부터 묶어가며 뺀다.
#     if idx_len < -1:
#         break_num = idx_len
#         idx_len = 0     # 초기화

#         # 이후에는 가장 작은 인덱스부터 채워온다.
#         while True:
#             idx_len += data[idx_len]
#             if idx_len > bound_line + 1:
#                 break
#             cnt_group += 1
#     if break_num < -1:
#         break
#     cnt_group += 1

# print("최종 결과 : {}".format(cnt_group))


########################### 2023-09-25 ##############################
# 오름차순 정렬, 단일 for문 
n = int(input())
nums = list(map(int, input().split()))
nums.sort() # 오름차순 정렬

result_cnt = 0
cnt = 0
for i in nums:
    cnt += 1
    if i == cnt:
        result_cnt += 1
        cnt = 0

print(result_cnt)

