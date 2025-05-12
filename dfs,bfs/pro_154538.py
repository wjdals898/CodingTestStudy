# 숫자 변환하기
from collections import deque


# bfs 방식 (dynamic programming 보다 시간 효율성 좋음)
def solution1(x, y, n):
    queue = deque()
    queue.append((0, y))    # (연산 횟수, 현재 수)
    visited = [0] * (y+1)   # 중복 체크를 위한 방문 처리 리스트

    while queue:
        count, num = queue.popleft()
        if num == x:    # x로 변환된 경우 answer에 연산 횟수 추가 후 다음 경우로 넘어가기
            return count

        if num - n >= x and visited[num-n] == 0:
            queue.append((count+1, num-n))
            visited[num-n] = 1
        if num % 2 == 0 and num // 2 >= x and visited[num//2] == 0:
            queue.append((count+1, num//2))
            visited[num//2] = 1
        if num % 3 == 0 and num // 3 >= x and visited[num//3] == 0:
            queue.append((count+1, num//3))
            visited[num//3] = 1

    return -1


# dynamic programming 방식
def solution2(x, y, n):

    dp = [float('inf')] * (y+1)     # dp 배열 초기화
    dp[x] = 0

    for i in range(x, y+1):     # x부터 y까지 1씩 증가시키면서 반복
        if i + n <= y:  # x에 n 더하기
            dp[i+n] = min(dp[i+n], dp[i] + 1)
        if i * 2 <= y:  # x에 2 곱하기
            dp[i*2] = min(dp[i*2], dp[i] + 1)
        if i * 3 <= y:  # x에 3 곱하기
            dp[i*3] = min(dp[i*3], dp[i] + 1)

    return dp[y] if dp[y] != float("inf") else -1


x_list = [10, 10, 2, 2, 1]
y_list = [40, 40, 5, 17, 1000000]
n_list = [5, 30, 4, 3, 1]
for x, y, n in zip(x_list, y_list, n_list):
    print(solution1(x, y, n))
