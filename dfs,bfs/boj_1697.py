# 숨바꼭질
from collections import deque


def solution1(n, k):
    visited = [False] * (100000 + 1)    # 중복 탐색 방지
    queue = deque([(n, 0)])     # (현재 위치, 걸린 시간)
    visited[n] = True   # 현재 위치 방문 처리

    while queue:
        x, sec = queue.popleft()

        if x == k:  # 동생의 위치에 도달한 경우 결과 리턴
            return sec

        for next_x in (x-1, x+1, x*2):  # 걷기(x-1, x+1), 순간이동(x*2)
            # 범위 내에 있거나 이전에 이동했던 위치가 아닌 경우
            if 0 <= next_x <= 100000 and not visited[next_x]:
                queue.append((next_x, sec+1))
                visited[next_x] = True


def solution2(n, k):
    print(k)
    if n >= k:  # n이 k보다 크면 걸어서 이동한 시간 반환
        return n - k
    if k == 1:  # 재귀적으로 탐색하다가 거리차가 1이된다.
        return 1
    if k % 2:   # k가 홀수인 경우 걷기로 이동
        return min(solution2(n, k-1), solution2(n, k+1))+1
    #  k가 짝수인 경우 걷기와 순간이동 중 짧은 시간 선택
    return min(k - n, solution2(n, k//2)+1)


n, k = map(int, input().split())
print(solution2(n, k))
