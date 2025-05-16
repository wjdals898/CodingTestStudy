# n^2 배열 자르기


def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)

    return answer


def solution2(n, left, right):
    answer = []

    for i in range(left // n, right // n + 1):
        tmp = [i+1] * (i+1) + [j for j in range(i + 2, n + 1)]

        if left//n == right//n:
            answer = tmp[left%n:right%n+1]
        else:
            if i == left // n:
                answer += tmp[left % n:]
            elif i == right // n:
                answer += tmp[:right % n+1]
            else:
                answer += tmp

    return answer


n_list = [3, 4, 4]
left_list = [2, 7, 4]
right_list = [5, 14, 6]
for n, left, right in zip(n_list, left_list, right_list):
    print(solution(n, left, right))
