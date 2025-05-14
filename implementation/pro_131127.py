# 할인 행사
from collections import Counter


def solution(want, number, discount):
    answer = 0
    want_dic = {w:n for w, n in zip(want, number)}  # {제품:수량}
    part_dic = Counter(discount[:9])    # 초기 구간 설정

    for i in range(9, len(discount)):
        part_dic[discount[i]] += 1  # 새로운 할인 제품 추가

        if want_dic == part_dic:    # 원하는 제품을 모두 할인 받는 경우
            answer += 1

        part_dic[discount[i-9]] -= 1    # 다음 구간 계산을 위해 첫 번째 제품 제외
        if part_dic[discount[i-9]] == 0:    # 필요 없는 항목 제거
            del part_dic[discount[i-9]]

    return answer


want_list = [
["banana", "apple", "rice", "pork", "pot"],
["apple"]
]
number_list = [
[3, 2, 2, 2, 1],
    [10]
]
discount_list = [
["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"],
["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
]
for want, number, discount in zip(want_list, number_list, discount_list):
    print(solution(want, number, discount))
