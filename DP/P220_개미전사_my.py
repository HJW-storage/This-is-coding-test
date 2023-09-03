n = int(input())
nums = list(map(int, input().split()))

def solution(n, nums):
    dp = [0] * n    # dp 테이블 생성
    # nums 리스트 인덱스 0부터 시작이니 n값도 -1 해줘서 인덱스 맞추자.
    # n = n -1
    
    # base case
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    dp[2] = max(dp[1], dp[0] + nums[2]) # n이 3일때, 따로 처리.
    
    for i in range(3, n):
        dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i])
        dp[i] = max(dp[i-1], dp[i])
        
    return dp[n-1]

print(solution(n, nums))