# K번째수

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        a = sorted(array[i-1:j])
        answer.append(a[k-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
