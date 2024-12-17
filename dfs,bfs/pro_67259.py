# 경주로 건설
from collections import deque

def solution(board):
    answer = float("inf")
    n = len(board)
    # 상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[[float("inf") for _ in range(4)] for _ in range(n)] for _ in range(n)]

    queue = deque()
    queue.append((0, 0, -1, 0))     # x, y, 방향, 비용
    while queue:
        x, y, prev_d, cost = queue.popleft()  # 현재 좌표 x, y, 방향, 비용
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 부지 크기를 넘는 경우 건너뛰기
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 벽이거나 시작점일 경우 건너뛰기
            if board[nx][ny] == 1 or (nx, ny) == (0, 0):
                continue
            # 현재 방향과 다음 이동 방향에 따라 비용 계산
            if prev_d != -1 and prev_d != i:
                new_cost = cost + 600
            else:
                new_cost = cost + 100
            # 도착점 여부 확인
            if (nx, ny) == (n - 1, n - 1):
                answer = min(answer, new_cost)
            elif visited[nx][ny][i] > new_cost:
                queue.append((nx, ny, i, new_cost))
                visited[nx][ny][i] = new_cost

    return answer


board_list = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
    [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
    [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
]
for data in board_list:
    print(solution(data))
