# N-Queen

def solution(n):

    def dfs(row, column, arr1, arr2):
        answer = 0
        if row == n:
            return answer + 1

        for i in range(n):
            # 현재 열, 대각선 방향에 퀸이 없으면
            if not column[i] and not arr1[row+i] and not arr2[n - i + row]:
                # 해당 자리에 퀸 놓고 대각선 방향 막기
                column[i], arr1[row+i], arr2[n - i + row] = True, True, True
                # 다음 행으로 이동하여 퀸 배치하기
                answer += dfs(row+1, column, arr1, arr2)
                # 해당 위치에 놓았던 퀸 없애기
                column[i], arr1[row + i], arr2[n - i + row] = False, False, False

        return answer

    return dfs(0, [False] * n, [False] * (n * 2), [False] * (n * 2))


n = 4
print(solution(n))
