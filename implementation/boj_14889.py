# 스타트와 링크
from sys import stdin


def calculate_value(team):
    value = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            value += arr[team[i]][team[j]] + arr[team[j]][team[i]]

    return value


def backtracking(depth, index, team1):
    global m
    if depth == n//2:
        team2 = [t for t in range(n) if t not in team1]
        value_s = calculate_value(team1)    # 스타트팀 점수 계산
        value_l = calculate_value(team2)    # 링크팀 점수 계산
        m = min(m, abs(value_s-value_l))
        return

    for i in range(index, n):
        team1.append(i)
        backtracking(depth+1, i+1, team1)
        team1.remove(i)


n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

m = float("inf")
backtracking(0, 0, [])
print(m)
