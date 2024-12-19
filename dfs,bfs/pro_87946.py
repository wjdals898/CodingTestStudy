# 피로도

def solution(k, dungeons):

    def dfs(remain, count, arr):
        count_max = count
        for index, dungeon in enumerate(dungeons):
            # 남아있는 피로도가 최소 필요 피로도보다 크면 탐험
            if remain >= dungeon[0] and index not in arr:
                arr.append(index)
                count_max = max(
                    count_max,
                    dfs(remain - dungeon[1], count+1, arr)
                )
                arr.remove(index)

        return count_max

    return dfs(k, 0, [])


kk = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(kk, dungeons))
