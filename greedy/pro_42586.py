# 기능개발
from math import ceil


def solution(progresses, speeds):
    answer = []
    day = 0

    for i in range(len(progresses)):
        if progresses[i] + speeds[i] * day >= 100:
            answer[-1] += 1
        else:
            day = ceil((100 - progresses[i]) / speeds[i])
            answer.append(1)

    return answer


progresses_list = [
    [93, 30, 55],
    [95, 90, 99, 99, 80, 99],
    [90, 90, 90],
    [95, 94, 93]
]
speeds_list = [
    [1, 30, 5],
    [1, 1, 1, 1, 1, 1],
    [1, 5, 4],
    [3, 3, 3]
]
for progresses, speeds in zip(progresses_list, speeds_list):
    print(solution(progresses, speeds))
