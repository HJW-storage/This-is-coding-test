# # 거스름 돈
# data = int(input())
# money = [500, 100, 50, 10]
# cnt = 0
# for i in range(len(money)):
#     cnt += data // money[i]
#     data = data % money[i]
#
# print(cnt)


# # 1이 될 때까지
# n, k = map(int, input().split())
# cnt = 0
# while True:
#     if n % k == 0:
#         n /= k
#         n = int(n)
#     else:
#         n -= 1
#     cnt += 1
#     if n == 1:
#         break
# print(cnt)

data = list(input())
print(data)
result = int(data[0])
for i in range(1,len(data)):
    if data[i] == '0' or result == 0:
        result += int(data[i])
    else:
        result *= int(data[i])
print(result)
