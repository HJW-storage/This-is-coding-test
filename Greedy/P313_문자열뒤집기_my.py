################### 2023-09-25 ###################
# 단일 for문
s = list(map(int, input()))

result = 0
cnt = 0
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        cnt += 1
        if cnt == 2:
            result += 1
            cnt = 0
            
print("최소 횟수 : {}".format(result))