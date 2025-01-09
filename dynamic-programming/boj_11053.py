# 가장 긴 증가하는 부분 수열
from sys import stdin


def solution(n, numbers):
    d = [1] * n

    for i in range(1, n):
        for j in range(i):
            if numbers[i] > numbers[j]:
                d[i] = max(d[i], d[j]+1)

    return max(d)


n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
print(solution(n, numbers))
