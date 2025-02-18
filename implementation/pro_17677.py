# 뉴스 클러스터링
from collections import Counter


def solution(str1, str2):
    answer = 0
    arr1 = make_multiset(str1)  # 다중 집합 만들기
    arr2 = make_multiset(str2)  # 다중 집합 만들기

    if len(arr1) == len(arr2) == 0:
        answer = 1
    else:
        cnt1 = Counter(arr1)
        cnt2 = Counter(arr2)

        a = sum((cnt1 & cnt2).values())  # & 연산으로 교집합 계산
        b = sum((cnt1 | cnt2).values())  # | 연산으로 합집합 계산

        answer = a / b

    return int(answer * 65536)


def make_multiset(str):
    arr = []

    for i in range(len(str)-1):
        s = str[i]+str[i+1]
        if s.isalpha():     # 영문자일 경우에만 집합에 추가
            arr.append(s.upper())

    return arr


str1_list = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
str2_list = ["french", "shake hands", "AAAA12", "e=m*c^2"]
for str1, str2 in zip(str1_list, str2_list):
    print(solution(str1, str2))
