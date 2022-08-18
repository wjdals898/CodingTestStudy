# 소수&팰린드롬
import math

N = int(input())

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(N,10000001):
    if i == 1: continue
    if str(i) == str(i)[::-1] and is_prime(i):
        print(1003001 if i == 0 else i)
        break
