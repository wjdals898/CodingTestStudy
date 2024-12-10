# 단어 퍼즐

def solution(strs, t):
    n = len(t)
    dp = [float("inf") for _ in range(n+1)]
    dp[0] = 0
    sizes = set([len(s) for s in strs]) # strs 값들의 길이 집합

    for i in range(1, n+1):
        for size in sizes:
            if t[i-size:i] in strs:
                dp[i] = min(dp[i], dp[i-size] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1


strs_list = [
    ["ba","na","n","a"],
    ["app","ap","p","l","e","ple","pp"],
    ["ba","an","nan","ban","n"]
]
t_list = ["banana", "apple", "banana"]
for i in range(len(strs_list)):
    print(solution(strs_list[i], t_list[i]))
