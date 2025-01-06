# 가장 큰 수

def solution(numbers):
    s_numbers = list(map(str, numbers))
    s_numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    answer = ''.join(s_numbers)
    return "0" if answer[0] == "0" else answer


numbers_list = [
    [6, 10, 2],
    [3, 30, 34, 5, 9],
    [0, 0, 0]
]
for data in numbers_list:
    print(solution(data))
