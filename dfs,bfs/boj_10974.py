# 모든 순열
from itertools import permutations

n = int(input())
arr = [a for a in range(1, n+1)]
global result
result = []


def dfs(n, arr, tmp):
    global result
    if len(tmp) == n:
        result.append(tmp.copy())
        return

    for a in arr:
        if a not in tmp:
            tmp.append(a)
            dfs(n, arr, tmp)
            tmp.remove(a)


for i in arr:
    dfs(n, arr, [i])

for r in result:
    print(' '.join(map(str, r)))


# 두 번째 방법 - 함수 사용
for per in permutations(range(1, n+1), n):
    print(' '.join(map(str, per)))
