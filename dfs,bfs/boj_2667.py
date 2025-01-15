# 단지 번호 붙이기
from sys import stdin
from collections import deque
import heapq

n = int(stdin.readline())
house = []
for _ in range(n):
    line = list(stdin.readline().split()[0])
    house.append(list(map(int, line)))

visited = [[False] * n for _ in range(n)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(cnt, x, y):
    queue = deque([(x, y)])
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나거나 0(집이 없는 곳)인 경우 건너뛰기
            if nx < 0 or nx >= n or ny < 0 or ny >= n or house[ny][nx] == 0:
                continue
            # 1(집이 있는곳)이고 방문하지 않은 집인 경우
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt


heap = []
for i in range(n):
    for j in range(n):
        if house[i][j] == 1 and not visited[i][j]:
            heapq.heappush(heap, bfs(1, j, i))

print(len(heap))
for _ in range(len(heap)):
    print(heapq.heappop(heap))
