# 연산자 끼워넣기
from sys import stdin


def backtracking(idx, operations, result):
    global r_min, r_max
    if idx == n:    # 모든 수를 계산한 경우
        r_min = min(r_min, result)
        r_max = max(r_max, result)
        return

    current = nums[idx]

    for i in range(4):
        if operations[i] != 0:
            operations[i] -= 1
            if i == 0:  # 더하기
                backtracking(idx+1, operations, result + current)
            elif i == 1:    # 빼기
                backtracking(idx+1, operations, result - current)
            elif i == 2:    # 곱하기
                backtracking(idx+1, operations, result * current)
            else:   # 나누기
                backtracking(idx+1, operations, cxx14_divide(result, current))

            operations[i] += 1


# C++14 기준 정수 나눗셈 구현
def cxx14_divide(a, b):
    if a < 0 < b:
        return -(abs(a) // b)
    elif a > 0 > b:
        return -(a // abs(b))
    else:
        return a // b


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
operations = list(map(int, stdin.readline().split()))
r_min, r_max = float("inf"), -float("inf")

backtracking(1, operations, nums[0])

print(r_max); print(r_min)
