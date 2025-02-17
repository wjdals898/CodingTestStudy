# 예상 대진표
from math import log2, ceil


def solution(n,a,b):

    d = int(log2(n))
    for i in range(d+1):
        if a == b:
            return i
        a = ceil(a/2)
        b = ceil(b/2)


N, A, B = 8, 4, 7
print(solution(N,A,B))
