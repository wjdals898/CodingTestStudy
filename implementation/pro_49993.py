# 스킬트리

def solution(skill, skill_trees):
    answer = 0

    for s in skill_trees:
        stack = ""
        for a in s:
            if a in skill:  # 선행 스킬에 있는 알파벳일 경우
                stack += a
        if stack == skill[:len(stack)]: # 선행 스킬 순서에 맞는지 검증
            answer += 1
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
