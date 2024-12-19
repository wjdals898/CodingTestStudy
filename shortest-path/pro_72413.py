# 합승 택시 요금
import heapq


def dijkstra(start, n, graph):
    visited = [float("inf") for _ in range(n + 1)]
    visited[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))  # (요금, 시작 노드)
    while heap:  # 연결 노드가 있는 동안 반복
        fare, node = heapq.heappop(heap)

        for next_node, next_fare in graph[node]:
            new_fare = fare + next_fare
            if new_fare < visited[next_node]:
                visited[next_node] = new_fare
                heapq.heappush(heap, (new_fare, next_node))

    return visited


def solution(n, s, a, b, fares):
    answer = float("inf")
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    from_s = dijkstra(s, n, graph)  # s부터 모든 지점으로 가는 비용
    from_a = dijkstra(a, n, graph)  # a부터 모든 지점으로 가는 비용
    from_b = dijkstra(b, n, graph)  # b부터 모든 지점으로 가는 비용

    for i in range(1, n+1):
        answer = min(answer, from_s[i] + from_a[i] + from_b[i])

    return answer


n_list = [6,7,6]
s_list = [4,3,4]
a_list = [6,4,5]
b_list = [2,1,6]
fares_list = [
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
    [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
]
for i in range(len(n_list)):
    print(solution(n_list[i], s_list[i], a_list[i], b_list[i], fares_list[i]))
