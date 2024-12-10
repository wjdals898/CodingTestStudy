# 가장 큰 정사각형 찾기

def solution(board):

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            # 1일 때만 길이 계산하기
            if board[i][j] == 1:
                # 왼쪽 위 대각선, 위쪽, 왼쪽 값 중 최솟값에 1(현재 값) 더하기
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    answer = max(max(row) for row in board)
    return answer ** 2


board_list = [
    [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]],
    [[0,0,1,1],[1,1,1,1]]
]
for data in board_list:
    print(solution(data))
