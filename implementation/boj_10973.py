# 이전 순열
N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if arr[i-1] > arr[i]:   # arr[i] ~ arr[N-1]까지는 오름차순 정렬
        for j in range(N-1, 0, -1):
            if arr[i-1] > arr[j]:   # i-1번째 수보다 작은 수 찾기
                arr[i-1], arr[j] = arr[j], arr[i-1]
                # i번째부터는 내림차순으로 정렬됨
                arr = arr[:i] + sorted(arr[i:], reverse=True)
                print(*arr)
                exit()
print(-1)
