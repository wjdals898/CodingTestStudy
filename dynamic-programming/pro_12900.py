# 2 x n 타일링

def solution(n):
    # 배치가능한 경우의 수 저장하는 리스트 0으로 초기화
    dp = [0] * (n + 1)
    dp[1] = 1   # 1인 경우 가능한 경우의 수 1로 초기화
    dp[2] = 2   # 2인 경우 가능한 경우의 수 2로 초기화

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[-1]


n_list = [4, 7]
for data in n_list:
    print(solution(data))
