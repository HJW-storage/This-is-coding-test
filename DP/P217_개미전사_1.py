n = int(input())
nums = list(map(int, input().split()))

def solution(n, nums):
    dp = [0] * n    # dp 테이블 생성
    
    # base case
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
    return dp[n-1]

print(solution(n, nums))