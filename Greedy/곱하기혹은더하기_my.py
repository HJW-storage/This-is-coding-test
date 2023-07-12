import sys
data = list(map(int, sys.stdin.readline().rstrip()))
print(data)

result = data[0]
# print(len(data))
for i in range(1, len(data)):
    if data[i] == 0:
        result += data[i]
    else:
        if data[i-1] == 0:
            result += data[i]
        else:
            result *= data[i]

print("최종 결과 : {}".format(result))