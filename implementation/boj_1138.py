# 한 줄로 서기

n = int(input())
people = list(map(int, input().split()))
result = [0 for _ in range(n)]

for i, p in enumerate(people):
    c = 0   # 0의 갯수 세기 위한 변수
    for j in range(n):
        if result[j] == 0:  # 해당 위치에 사람이 없는 경우
            # 이전까지의 빈 자리 수와 본인 왼쪽 사람 수가 일치할 경우
            if c == p:
                result[j] = i+1     # j번째 자리에 배정
                break
            c += 1

print(' '.join(map(str, result)))
