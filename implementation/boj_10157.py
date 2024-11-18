# 자리배정

c, r = map(int, input().split())
k = int(input())
dx = [0, 1, 0, -1]  # 위, 오른, 아래, 왼
dy = [-1, 0, 1, 0]  # 위, 오른, 아래, 왼
direction = 0
visited = [[0 for _ in range(r)] for _ in range(c)]
num = c * r # 총 좌석 수


def turn_right():   # 방향 전환
    global direction
    direction += 1
    if direction == 4:
        direction = 0


cnt = 1
x, y = 0, r-1
visited[x][y] = 1 # 처음 자리 방문 표시
while True:
    # k번째 사람이거나 자리 수보다 클 경우 반복문 종료
    if cnt == k or num < k:
        break

    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or nx >= c or ny < 0 or ny >= r:  # 공연장 크기 벗어나는 경우
        turn_right()
    else:
        if visited[nx][ny] == 0:    # 빈 좌석인 경우
            visited[nx][ny] = 1
            x, y = nx, ny
            cnt += 1
        else:
            turn_right()

print(f'{x+1} {r-y}' if num >= k else 0)
