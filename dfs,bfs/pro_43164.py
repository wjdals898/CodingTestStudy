# 여행경로
from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    # graph 알파벳 역순으로 정렬
    for g in graph:
        graph[g].sort(reverse=True)

    def dfs(city):
        while graph[city]:
            next_city = graph[city].pop()
            dfs(next_city)
        answer.append(city)

    dfs("ICN")
    return answer[::-1]


tickets_list = [
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
]
for data in tickets_list:
    print(solution(data))
