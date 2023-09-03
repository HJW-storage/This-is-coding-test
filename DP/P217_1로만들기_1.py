# DP 바텀업 방식

x = int(input()) 

# 만약 탑다운 방식 재귀함수로 코드를 짜면 5, 3, 2, 1 나눠지는 우선순위로 구성했을 것이다.
# 바텀업 방식이므로 역순으로 1, 2, 3, 5로 조사하며 최소값을 비교하며 답을 쌓는다. 
def solution(x):
    dp = [0] * (x+1)  # dp 테이블 생성
    
    for i in range(2, x+1):
        # 1을 빼는 경우
        dp[i] = dp[i-1] + 1
        # 2로 나누는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        # 3로 나누는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        # 5로 나누는 경우
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i//5] + 1)
        
    return dp[x]

print(solution(x))

    