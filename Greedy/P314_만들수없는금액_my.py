################### 2023-09-25 ###################
from itertools import combinations

data = [3, 5, 6, 2, 9]
cost = []
for i in range(1, len(data)+1):
    result = list(combinations(data, i))
    for j in range(len(result)):
        cost.append(sum(result[j]))
    # print(result)
# print(result)
# print(sum(result[0]), len(result))
cost = set(cost)
print(cost)

for i in range(1, 1001):
    if i not in cost:
        print("동전들로 만들 수 없는 양의 정수 금액 중 최솟값 : {}".format(i))
        break

