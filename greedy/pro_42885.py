# 구명보트

def solution(people, limit):
    answer = 0
    l, r = 0, len(people)-1
    people.sort()

    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        answer += 1

    return answer


people_list = [
[70, 50, 80, 50],
[70, 80, 50]
]
limit_list = [100, 100]
for p, l in zip(people_list, limit_list):
    print(solution(p, l))
