# 멀리 뛰기

# dp 배열 이용
def solution(n):
    dp = [1] * (n+1)
    dp[1] = 2

    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n-1]


# 변수 두 개로 경우의 수 구하기(피보나치 수)
def solution2(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, (a+b) % 1234567

    return b


n_list = [4,3,1,+2,5,6]
for n in n_list:
    print(solution2(n))
