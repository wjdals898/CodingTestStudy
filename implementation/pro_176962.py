# 과제 진행하기

def solution(plans):
    answer = []
    stop_works = []
    l = len(plans)

    for p in plans:
        p[1] = int(p[1][:2]) * 60 + int(p[1][3:])   # 숫자로 변환
        p[2] = int(p[2])

    plans.sort(key=lambda x: x[1])  # 시작 시간 순으로 정렬

    for i in range(l):
        end_time = plans[i][1] + plans[i][2]
        new_start = plans[i][1]

        if i == l-1:    # 마지막 과제는 끝까지 수행
            new_start = float("inf")
        else:
            new_start = plans[i+1][1]

        # 현재 과제 진행 중 새로운 과제를 시작 해야 하는 경우
        if end_time > new_start:
            stop_works.append((plans[i][0], end_time-new_start))
        # 다음 과제 시작 시간 전에 현재 과제가 끝날 경우
        else:
            answer.append(plans[i][0])  # 끝난 과제에 추가
            # 새로운 과제 시작 전에 현재 과제가 끝난 경우 중단된 과제 진행
            if end_time < new_start:
                while stop_works and end_time < new_start:
                    name, playtime = stop_works.pop()
                    end_time += playtime

                    if end_time > new_start:
                        stop_works.append((name, end_time-new_start))
                        break
                    else:
                        answer.append(name)

    return answer


plans_list = [
[["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]],
[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]],
[["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
]
for pla in plans_list:
    print(solution(pla))
