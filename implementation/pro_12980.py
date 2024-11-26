# 점프와 순간 이동

def solution(n):
    ans = 0
    while n > 0:    # n을 2로 나눈 값이 0이 될 때까지 반복
        if n % 2 == 1:  # 나머지가 1이면 1칸 점프
            ans += 1
        n //= 2

    return ans

def solution2(n):
    # 2로 계속 나눈 나머지를 합하면 2진수 이므로 2진수값에서 1을 찾으면 됨
    return bin(n).count('1')

arr = [5, 6, 5000]
for a in arr:
    print(solution2(a))
