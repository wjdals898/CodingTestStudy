# 숫자의 표현

# 완전 탐색(브루트 포스)
def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        total = 0

        while total < n:
            total += i  # i부터 합 구하기
            if total == n:  # 일치하면 다음 구간으로 진행
                answer += 1
                break
            i += 1  # total이 n보다 같거나 클 때까지 증가하며 합 구하기

    return answer


# 투 포인터 사용
def solution2(n):
    answer = 1
    start, end = 1, 1
    total = 1

    while n > 2 and start <= n//2 + 1:
        if total < n:   # 구간의 합이 n보다 작으면 새로운 숫자 추가
            end += 1
            total += end
        elif total > n:     # 구간의 합이 n보다 크면 시작 숫자 제거
            total -= start
            start += 1
        else:   # 구간의 합이 n과 일치하면 시작 숫자 제거 후 다음 구간 진행
            answer += 1
            total -= start
            start += 1

    return answer


n = 15
print(solution2(n))
