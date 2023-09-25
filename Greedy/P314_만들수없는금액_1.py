# 해설 P509
################### 2023-09-25 ################### 
n = int(input())
coins = list(map(int, input().split()))
coins.sort()    # 오른차순 정렬

target = 1
for i in coins:
    if target < i:
        break
    else:
        target += i
        
print(target)
