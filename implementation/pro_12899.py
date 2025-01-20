# 124 나라의 숫자

def solution(n):
    answer = ''
    while n > 0:
        tmp = n % 3
        if tmp == 0:
            answer = '4' + answer
            n = n // 3 - 1
        else:
            answer = str(tmp) + answer
            n //= 3

    return answer


n_list = [1,2,3,4,5,6,7,8,9,10,13]
for n in n_list:
    print(solution(n))
