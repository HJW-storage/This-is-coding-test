# import sys
# data = list(map(int, sys.stdin.readline().rstrip()))
# print(data)

# result = data[0]
# # print(len(data))
# for i in range(1, len(data)):
#     if data[i] == 0:
#         result += data[i]
#     else:
#         if data[i-1] == 0:
#             result += data[i]
#         else:
#             result *= data[i]

# print("최종 결과 : {}".format(result))


################### 2023-09-25 ###################
s = list(input())
s = list(s) # 문자열 형태로 리스트 저장
result = 0

for i in s:
    if result == 0 or i == '0':
        result += int(i)
    else:
        result *= int(i)
        
print(result)
