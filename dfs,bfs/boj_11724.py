# 연결 요소의 개수
from collections import deque
from sys import stdin


def solution(n, graph):
    answer = 0
    visited = [False] * (n+1)

    def bfs(start, visited, graph):
        visited[start] = True
        queue = deque([start])

        while queue:
            current = queue.popleft()

            for node in graph[current]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

    for i in range(1, n+1):
        if not visited[i]:
            bfs(i, visited, graph)
            answer += 1

    return answer


n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

print(solution(n, graph))
