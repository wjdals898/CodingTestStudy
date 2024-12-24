# 외벽 점검
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)

    # 시작점 변경해 가며 친구 투입
    for i in range(length):
        # 친구 수만큼 가능한 순열
        for per in permutations(dist, len(dist)):
            cnt = 1
            # 현재 투입된 친구가 이동하는 위치
            position = weak[i] + per[cnt-1]

            for j in range(i, i+length):
                # 현재 친구로 끝까지 도달하지 못하면 다음 친구 투입
                if position < weak[j]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    # 다음 친구가 이동하는 위치
                    position = weak[j] + per[cnt-1]
            answer = min(answer, cnt)

    return answer if answer <= len(dist) else -1


weak_list = [
    [1, 5, 6, 10],
    [1, 3, 4, 9, 10]
]
dist_list = [
    [1, 2, 3, 4],
    [3, 5, 7]
]
for i in range(2):
    print(solution(12, weak_list[i], dist_list[i]))
