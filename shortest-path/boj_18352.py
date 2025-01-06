# 특정 거리의 도시 찾기
import heapq
import sys


def dijkstra(start, n, k, graph):
    visited = [float('inf') for _ in range(n+1)]
    visited[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))    # (거리, 시작 노드)
    while heap:     # 연결 노드가 있는 동안 반복
        dist, node = heapq.heappop(heap)

        for next_node in graph[node]:   # 시작 노드와 연결된 노드들
            new_dist = dist + 1     # a에서 b로 가는 거리는 1로 동일
            # 새로 구한 거리가 더 짧을 경우 최단 거리 갱신
            if new_dist < visited[next_node]:
                visited[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    result = []
    for index, v in enumerate(visited):
        if v == k:
            result.append(index)
    return result if len(result) > 0 else -1


n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

answer = dijkstra(x, n, k, graph)
if answer == -1:
    print(answer)
else:
    for i in answer:
        print(i)
