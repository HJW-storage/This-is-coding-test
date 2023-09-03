n = int(input())

def solution(n):
    dp = [0] * (n+1)    # dp 테이블 생성
    
    dp[1] = 1   # base case
    dp[2] = 3   # base case

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] * 2   # 점화식
        
    return dp[n]

result = solution(n) % 796796
print(result)
    
    
    