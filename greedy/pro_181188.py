# 요격 시스템

def solution(targets):
    answer = 0
    x = 0   # 마지막 미사일 위치
    print(sorted(targets, key=lambda t: t[1]))

    for s, e in sorted(targets, key=lambda t: t[1]):
        if s >= x:  # 이전 미사일 범위 내에 없는 경우 새로운 미사일 필요
            answer += 1
            x = e
    return answer


targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))
