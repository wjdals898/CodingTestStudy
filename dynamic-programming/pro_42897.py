# 도둑질

def solution(money):
    a1, b1, c1 = money[0], money[1], money[0] + money[2]
    a2, b2, c2 = 0, money[1], money[2]

    for i in range(3, len(money)):
        # 첫번째 집을 방문한 경우
        a1, b1, c1 = b1, c1, max(a1, b1) + money[i]
        # 첫번째 집을 방문하지 않은 경우
        a2, b2, c2 = b2, c2, max(a2, b2) + money[i]

    # a1, b1은 첫번째 집을 방문한 경우 돈의 최댓값
    # c2는 첫번째 집을 방문하지 않은 경우 돈의 최댓값
    return max(a1, b1, c2)


money_list = [
    [1, 2, 3, 1],
    [3, 1, 5, 4],
    [2, 5, 1, 1],
    [100, 1, 1],
    [1, 100, 1],
    [1, 1, 100]
]
for data in money_list:
    print(solution(data))
