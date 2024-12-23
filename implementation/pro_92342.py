# 양궁대회
from itertools import combinations_with_replacement
from collections import Counter


def calculate_diff(cnt, info):
    a_score, b_score = 0, 0

    for i in range(11):
        # 둘 다 0인 경우 계산하지 않음
        if info[10 - i] == cnt[i] == 0:
            continue
        # 어피치 >= 라이언
        elif info[10-i] >= cnt[i]:
            a_score += i
        # 어피치 < 라이언
        elif info[10-i] < cnt[i]:
            b_score += i

    # 두 점수 차이 리턴(어피치 점수가 더 클 경우 -1 리턴)
    return b_score - a_score if b_score - a_score > 0 else -1


def solution(n, info):
    answer = [0] * 11
    max_diff, max_result = 0, {}

    # 0 ~ 10까지 숫자로 n 개의 원소를 만들 수 있는 조합
    for combi in combinations_with_replacement(range(11), n):
        cnt = Counter(combi)    # 각 원소의 개수 세기
        diff = calculate_diff(cnt, info)    # 라이언과 어피치의 점수차
        if diff > max_diff:     # 최대차일 경우 갱신
            max_diff = diff
            max_result = cnt

    if max_diff > 0:    # 라이언이 이기는 경우 점수별 화살 개수 세팅
        for n in max_result:
            answer[10-n] = max_result[n]
        return answer
    else:
        return [-1]


n_list = [5,1,9,10]
info_list = [
    [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1,0,0,0,0,0,0,0,0,0,0],
    [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1],
    [0,0,0,0,0,0,0,0,3,4,3]
]
for i in range(len(n_list)):
    print(solution(n_list[i], info_list[i]))
