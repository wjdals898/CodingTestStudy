# 정수 삼각형

def solution(triangle):
    n = len(triangle)
    # 삼각형 배열과 같은 리스트 0으로 초기화
    dp = [[0] * len(t) for t in triangle]
    dp[0][0] = triangle[0][0]  # 꼭대기 숫자 초기화

    for i in range(1, n):
        m = len(triangle[i])
        for j in range(m):
            # 가장 왼쪽 노드일 경우
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][0]
            # 가장 오른쪽 노드일 경우
            elif j == m-1:
                dp[i][j] = triangle[i][j] + dp[i - 1][-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[-1])


data = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(data))
