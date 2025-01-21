# 포도주 시식
from sys import stdin

n = int(stdin.readline())
glasses = []
for _ in range(n):
    glasses.append(int(stdin.readline()))

# a=연속으로 마신 경우, b=앞에 잔은 마시지 않은 경우, c=이전 a,b,c 중 최대값
a, b, c = glasses[0], glasses[0], 0
for i in range(1, n):
    a, b, c = b+glasses[i], c+glasses[i], max(a, b, c)

print(max(a, b, c))
