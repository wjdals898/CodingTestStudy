# 순위

def solution(n, results):
    answer = 0
    graph = [[0] * n for _ in range(n)]

    # 승패 정보 저장
    for a, b in results:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j: continue # 자기 자신은 제외
                if graph[i][j] != 0: continue   # 이미 값이 있으면 제외
                if graph[i][k] == 1 and graph[k][j] == 1:   # i > k > j 순일 때
                    graph[i][j] = 1
                    graph[j][i] = -1

    for g in graph:
        if g.count(0) == 1: # 자기 자신 이외에 승패를 알고 있음
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
