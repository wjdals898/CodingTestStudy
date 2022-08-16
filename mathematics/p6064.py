# 카잉 달력
T = int(input())

for i in range(T):
    M,N,x,y = map(int, input().split())
    k = -1
    for j in range(x,M*N+1,M):
        if (y-j)%N == 0:
            k = j; break
    print(k)
