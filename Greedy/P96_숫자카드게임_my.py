# # import sys
# n, m = map(int, input().split())

# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#     # arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# # print(arr)
# temp_arr = []
# for i in range(n):
#     temp_arr.append(min(arr[i]))

# # print(temp_arr)
# print("최종 결과 : {}".format(max(temp_arr)))

######################### 2023-10-25 #########################
n, m = map(int, input().split())
card_game = []
min_nums = []   # 카드 게임 각 행의 최소값을 저장할 리스트 선언

for i in range(n):
    card_game.append(list(map(int, input().split())))
    min_nums.append(min(card_game[i]))    
# print(card_game)
# print(min_nums)

result = max(min_nums)
print(result)