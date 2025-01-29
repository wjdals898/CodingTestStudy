# 쉬운 계단 수

n = int(input())
dp = [[0] * 10 for _ in range(n)]
dp[0][1:] = [1] * 9     # 첫 자리 숫자 개수 초기화

for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1]) % 1000000000)
