# 소수 찾기
from math import sqrt
from itertools import permutations


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        # 1과 자기 자신 이외에 나눠지는 수 있을 경우
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    strs = list(numbers)
    result = []
    for i in range(1, len(numbers)+1):
        # 모든 순열에서 가능한 숫자 만들기
        for per in set(permutations(strs, i)):
            n = int(''.join(map(str, per)))
            # 이미 확인한 숫자는 제외하고 소수 판별
            if n not in result and is_prime(n):
                result.append(n)
                answer += 1

    return answer


numbers_list = ["17", "011", "001", "121", "144"]
for num in numbers_list:
    print(solution(num))
