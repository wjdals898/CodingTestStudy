# 배달
import heapq

def solution(N, road, K):
    # 각 마을에 연결된 마을 저장하는 리스트
    graph = [[] for _ in range(N+1)]
    # 1번 마을에서 각 마을까지 가는 시간 저장하는 리스트
    times = [float("inf") for _ in range(N+1)]
    times[1] = 0

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    heap = []
    # 첫 번째 마을 저장(시간, 노드) - 시간의 오름차순으로 heap에 저장
    heapq.heappush(heap, (0, 1))
    while heap:
        time, node = heapq.heappop(heap)

        for n, t in graph[node]:    # 현재 마을과 연결된 마을
            if times[node]+t < times[n]:
                heapq.heappush(heap, (t, n))
                times[n] = times[node]+t

    return sum(1 for time in times if time <= K)


n_list = [5, 6]
road_list = [
    [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],
    [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
]
k_list = [3, 4]
for i in range(len(n_list)):
    print(solution(n_list[i], road_list[i], k_list[i]))
