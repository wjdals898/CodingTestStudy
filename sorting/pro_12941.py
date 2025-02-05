# 최솟값 만들기

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        answer += a*b   # A 배열의 작은 수와 B 배열의 큰 수 곱하기

    return answer


A_list = [
    [1,4,2], [1,2]
]
B_list = [
    [5,4,4], [3,4]
]
for a, b in zip(A_list, B_list):
    print(solution(a, b))
