# 다음 큰 숫자


def solution(n):
    b = bin(n)[2:]
    c = b.count("1")
    if b[:c].count("0") == 0:   # 자릿수가 바뀐다면 맨 앞에 0 추가
        b = "0" + b

    m = 0
    for i in range(1,len(b)):
        if b[i-1] == "0" and b[i] == "1":   # 01일 때 10으로 바꾸기
            m = i

    answer = b[:m-1] + "10" + "0"*(b[m+1:].count("0")) + "1"*(b[m+1:].count("1"))

    return int(answer, 2)


def solution2(n):
    c = bin(n).count("1")
    while True:
        n += 1
        if bin(n).count("1") == c:
            break
    return n


n_list = [78, 15]
for n in n_list:
    print(solution2(n))
