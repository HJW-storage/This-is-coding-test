# 완전탐색으로 풀기. 
N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(int(input()))

# arr.sort()   # 내림차순 정렬. O(NlogN) 
# print(arr)

def solution(n, target):
    dp = [10001] * (target+1)
    dp[0] = 0
    
    for i in range(n):
        for j in range(arr[i], target+1):
            if dp[j-arr[i]] != 10001:
                dp[j] = min(dp[j], dp[j-arr[i]] + 1)
                
    if dp[target] == 10001:
        return -1
    else:
        return dp[target]

print("결과는 : {}".format(solution(N, M)))
