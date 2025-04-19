# 연속된 부분 수열의 합

def solution(sequence, k):
    l = len(sequence)
    answer = [0, l - 1]
    start, end = 0, 0   # 부분 수열 구간의 시작, 끝 인덱스
    s = sequence[0]     # 부분 수열의 합

    while end < l:
        if s < k:
            end += 1
            if end < l:
                s += sequence[end]
        else:
            if s == k and end-start < answer[1]-answer[0]:
                answer = [start, end]
            s -= sequence[start]
            start += 1

    return answer


sequence_list = [
    [1, 2, 3, 4, 5],
    [1, 1, 1, 2, 3, 4, 5],
    [2, 2, 2, 2, 2]
]
k_list = [7,5,6]
for se, k in zip(sequence_list, k_list):
    print(solution(se, k))
