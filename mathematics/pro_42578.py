# 의상

def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = 2
        else:
            dic[c[1]] += 1

    for v in dic.values():
        answer *= v

    return answer - 1   # 한 개도 착용하지 않는 경우 제외


clothes_list = [
    [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
]
for clothes in clothes_list:
    print(solution(clothes))
