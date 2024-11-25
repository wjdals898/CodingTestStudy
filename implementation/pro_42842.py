# 카펫
def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0: # 약수인 경우
            yw, yh = yellow//i, i   # 노란색 격자의 가로와 세로
            # 갈색의 가로와 세로는 노란색의 가로와 세로보다 항상 2씩 큼
            if (yw + 2) * 2 + yh * 2 == brown:
                answer = [yw+2, yh+2]
                break

    return answer


# 테스트
browns = [10, 8, 24]
yellows = [2, 1, 24]
for b, y in zip(browns, yellows):
    print(solution(b, y))
