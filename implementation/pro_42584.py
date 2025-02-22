# 주식 가격

def solution(prices):
    answer = [0] * len(prices)
    stack = []  # 떨어지지 않은 주식 가격의 인덱스를 저장하는 스택

    for i in range(len(prices)):
        # 스택의 마지막 인덱스의 주식 가격이 현재 가격보다 큰 경우
        # 현재(i) 가격이 스택에 있는 주식 가격보다 떨어진 경우
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx   # 기간 계산
        stack.append(i)

    # 가격이 끝까지 떨어지지 않은 경우(스택에 해당 인덱스가 남아 있음)
    for i in stack:
        answer[i] = len(prices) - i - 1

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
