# import sys
n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    # arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# print(arr)
temp_arr = []
for i in range(n):
    temp_arr.append(min(arr[i]))

# print(temp_arr)
print("최종 결과 : {}".format(max(temp_arr)))