# 방문 길이

# set 사용
def solution1(dirs):
    s = set()
    direction = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    curr_x, curr_y = 0, 0

    for d in dirs:
        dx, dy = direction[d]
        next_x, next_y = curr_x+dx, curr_y+dy

        # 범위 내에 있는지 검증
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            s.add((curr_x, curr_y, next_x, next_y))
            s.add((next_x, next_y, curr_x, curr_y))
            # 현재 위치 갱신
            curr_x, curr_y = next_x, next_y

    return len(s) // 2  # 같은 길이 두 개 저장되어 있기 때문에 2로 나누기


# visited 리스트 사용
def solution2(dirs):
    answer = 0
    direction = {"U": (0, 0, 1), "D": (1, 0, -1), "R": (2, 1, 0), "L": (3, -1, 0)}
    visited = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]   # 각 좌표별 [U,D,R,L] 방문 여부 저장
    current = (5, 5)    # 처음 시작 위치(x,y)

    for d in dirs:
        index, dx, dy = direction[d]   # 이동 방향
        next_x, next_y = current[0]+dx, current[1]+dy   # 이동할 좌표
        next_d = 0

        # 범위 밖인 경우 다음 명령어로
        if next_x < 0 or next_x > 10 or next_y < 0 or next_y > 10:
            continue

        if d == "U":
            next_d = 1
        elif d == "D":
            next_d = 0
        elif d == "R":
            next_d = 3
        elif d == "L":
            next_d = 2

        # 방문하지 않은 길인 경우
        if visited[next_y][next_x][next_d] == 0:
            answer += 1

        visited[current[1]][current[0]][index] = 1  # 현재 위치 방향 방문 처리
        visited[next_y][next_x][next_d] = 1     # 다음 위치 방향 방문 처리

        current = (next_x, next_y)  # 현재 위치 갱신

    return answer


dirs = ["ULURRDLLU", "LULLLLLLU"]
for d in dirs:
    print(solution1(d))
