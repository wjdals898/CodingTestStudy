# 피보나치 수

def solution(n):
    # 피보나치 수 리스트 0으로 초기화
    dp = [0 for _ in range(n+1)]
    dp[1] = 1

    # 2번째부터 n번째까지 피보나치 수 구하기
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    # n번째 수를 1234567로 나눈 나머지 값 반환
    return dp[-1] % 1234567


def solution2(n):
    a, b = 0, 1     # 초기 데이터는 0, 1번째 피보나치 수

    # n번째까지 피보나치 수 구하기
    for i in range(2, n+1):
        a, b = b, a + b     # a = i-1번째 수, b = i번째 수

    return b % 1234567


n_list = [3, 5, 6]
for data in n_list:
    print(solution2(data))
