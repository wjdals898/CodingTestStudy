# 귤 고르기
from collections import Counter


def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    s = 0
    for i, t in enumerate(sorted(counter.values(), reverse=True)):
        s += t
        if s >= k:
            answer = i + 1
            break
    return answer


k_list = [6,4,2]
tangerine_list = [
[1, 3, 2, 5, 4, 5, 2, 3],
[1, 3, 2, 5, 4, 5, 2, 3],
[1, 1, 1, 1, 2, 2, 2, 3]
]
for k, tangerine in zip(k_list, tangerine_list):
    print(solution(k, tangerine))
