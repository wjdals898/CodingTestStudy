# 소수 찾기
n = int(input())
arr = list(map(int, input().split()))
answer = 0
for a in arr:
    c = 0
    for i in range(1,a+1):
        if a % i == 0:
            c += 1
    if c == 2: answer += 1
print(answer)