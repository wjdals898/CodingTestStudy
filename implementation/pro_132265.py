# 롤케이크 자르기

from collections import Counter


def solution(topping):
    answer = 0  # 결과값 저장 변수
    topping_counter = Counter(topping)  # 토핑 가짓수
    half_topping = set()

    for t in topping:
        half_topping.add(t) # 절반에 토핑 추가
        topping_counter[t] -= 1 # 토핑 가짓수 줄이기

        # 토핑 가짓수가 0이면 딕셔너리에서 지우기
        if topping_counter[t] == 0:
            topping_counter.pop(t)

        # 절반 토핑 가짓수와 나머지 토핑 가짓수가 같으면 공평한 경우
        if len(half_topping) == len(topping_counter):
            answer += 1

    return answer


toppings = [
    [1, 2, 1, 3, 1, 4, 1, 2],
    [1, 2, 3, 1, 4]
]

for topping in toppings:
    print(solution(topping))
