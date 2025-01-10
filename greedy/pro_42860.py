# 조이스틱
def solution(name):
    answer = 0
    l = len(name)

    # 알파벳 변경 조작 횟수
    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

    move = l - 1    # 오른쪽으로 이동하는 경우(기본)

    for i in range(l):
        next = i + 1    # A가 연속되는 인덱스
        while next < l and name[next] == 'A':
            next += 1

        # (기본, 연속된 A의 왼쪽 시작, 연속된 A의 오른쪽 시작)
        move = min(move, i * 2 + l - next, 2 * (l - next) + i)

    return answer + move


names = ["JEROEN", "JAN", "ABAABAAAAB", "AABA"]
for name in names:
    print(solution(name))
