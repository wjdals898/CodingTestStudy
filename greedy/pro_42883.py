# 큰 수 만들기

def solution(number, k):
    stack = []

    for n in number:
        # 스택에서 숫자 삭제하는 경우
        # - 삭제 가능 횟수(k)가 남아있을 때
        # - 스택에 저장된 숫자가 1개 이상일 때(삭제할 숫자가 있을 때)
        # - 현재 숫자가 스택의 마지막 숫자보다 클 때(스택의 뒤에서부터 숫자를 제거하고 현재 숫자를 넣어 더 큰 수를 만들 수 있음)
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    # 삭제 가능 횟수(k)가 남아있는 경우 스택의 뒤에서부터 k개를 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


number_list = ["1924", "1231234", "4177252841", "720378", "10000"]
k_list = [2, 3, 4, 2, 2]
for n, k in zip(number_list, k_list):
    print(solution(n, k))
