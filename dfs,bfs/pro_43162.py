# 네트워크

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    for i in range(n):
        if visited[i] == 0: # 방문하지 않은 노드인 경우
            dfs(computers, visited, i)  # 현재 노드부터 연결된 노드 탐색하며 방문 처리
            answer += 1

    return answer


def dfs(computers, visited, current):
    visited[current] = 1    # 현재 노드 방문 처리
    for j in range(len(computers[current])):
        # 현재 노드와 연결되어 있고 방문하지 않은 노드인 경우
        if computers[current][j] == 1 and visited[j] == 0:
            dfs(computers, visited, j)


n_list = [3, 3]
computers_list = [
    [[1, 1, 0], [1, 1, 0], [0, 0, 1]],
    [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
]
for i in range(len(n_list)):
    print(solution(n_list[i], computers_list[i]))
