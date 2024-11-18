# 이진 변환 반복하기
def solution(s):
    conversion_cnt = 0
    remove_cnt = 0
    while s != "1": # s가 1이 될 때까지 반복
        remove_cnt += s.count("0")  # 1-1. s에서 0의 개수 세기
        l = len(s.replace("0", "")) # 1-2. s에서 0 지우기
        s = format(l, 'b')  # 0을 지운 s의 길이를 2진수 변환
        conversion_cnt += 1
    return [conversion_cnt, remove_cnt]


arr = ["110010101001", "01110", "1111111"]

for s in arr:
    print(solution(s))
