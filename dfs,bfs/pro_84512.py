# 모음사전
from itertools import product


def solution1(word):
    global answer
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']

    def dfs(curr):
        global answer
        answer += 1
        if curr == word:
            return True
        if len(curr) == 5:
            return False
        for alpha in alphabet:
            if dfs(curr+alpha):
                return True

    for alpha in alphabet:
        if dfs(alpha):
            return answer


def solution2(word):
    arr = []
    alphabet = ['A', 'E', 'I', 'O', 'U']

    for i in range(1,6):
        for l in product(alphabet, repeat=i):
            arr.append(''.join(l))
    arr.sort()

    return arr.index(word) + 1



word_list = ["AAAAE", "AAAE", "I", "EIO"]
for data in word_list:
    print(solution2(data))
