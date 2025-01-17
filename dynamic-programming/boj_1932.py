# 정수 삼각형

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, n):   # 행 탐색
    for j in range(i+1):  # 열 탐색
        if j == 0:  # 첫 번째 열이면
            graph[i][0] += graph[i-1][0]
        elif j == i:  # 마지막 열이면
            graph[i][j] += graph[i-1][j-1]
        else:
            graph[i][j] += max(graph[i-1][j-1:j+1])

print(max(graph[-1]))
