# 부분수열의 합

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    for per in combinations(arr, i):
        if sum(per) == s:
            cnt += 1
print(cnt)
