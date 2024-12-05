# LCS 길이 계산하기

def solution(str1, str2):
    m = len(str1)
    n = len(str2)
    # LCS 저장할 테이블 초기화
    dp = [[0] * (n+1) for _ in range(m+1)]

    # 동적 프로그래밍으로 LCS 계산
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i - 1] == str2[j - 1]:    # 비교하는 문자가 같으면
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:   # 비교하는 문자가 같지 않으면
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


str1_list = ["ABCBDAB", "AGGTAB"]
str2_list = ["BDCAB", "GXTXAYB"]
for i in range(len(str1_list)):
    print(solution(str1_list[i], str2_list[i]))
