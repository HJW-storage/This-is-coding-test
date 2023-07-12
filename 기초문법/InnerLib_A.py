# eval : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
# data = eval("(3.1 + 5) * 6")
# print(data)
# print(type(data))

# arr = [9, 1, 8, 5, 4]
# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print(arr)

# result = sorted([9, 1, 8, 5, 4])
# print(result)
# result = sorted([9, 1, 8, 5, 4], reverse=True)
# print(result)

# res = sorted([("홍길동", 35), ("이순신", 75), ("아무개", 50)], key = lambda y: y[1], reverse=False)
# print(res)

# arr_name = [("홍길동", 35), ("이순신", 75), ("아무개", 50)]
#
# def my_key(x):
#     return x[1]
#
# print(sorted(arr_name, key=my_key))
# print(sorted(arr_name, key=lambda x: x[1]))

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# result = list(map(lambda a, b: a + b, list1, list2))
# print(result)

from collections import Counter
c_list = ['red', 'blue', 'red', 'green', 'blue', 'blue']
counter = Counter(c_list)
print(counter['blue'])
print(dict(counter))
print(counter)