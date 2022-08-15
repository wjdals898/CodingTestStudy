# 골드바흐의 추측
import sys

x = [0,0]+[1]*999999

def goldbach(n):
    for i in range(3,n//2+1,2):
        if x[i] and x[n-i]:
            return f'{n} = {i} + {n-i}'
    return "Goldbach's conjecture is wrong."

for i in range(3,1000001,2):
    if x[i]:
        for j in range(2*i, 1000001, i):
            x[j] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    print(goldbach(n))