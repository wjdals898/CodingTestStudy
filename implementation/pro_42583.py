# 다리를 지나는 트럭
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)    # 다리를 건너지 않은 트럭
    bridge = deque()    # 다리 위에 있는 트럭
    current_weight = 0  # 다리 위에 있는 트럭의 무게 합

    while queue or bridge:
        answer += 1

        # 다리 위의 모든 트럭의 남은 거리 감소시키기
        bridge = deque([(length - 1, w) for length, w in bridge])

        # 다리를 지난 트럭 제거
        if bridge and bridge[0][0] == 0:
            current_weight -= bridge[0][1]
            bridge.popleft()

        # 다리 위에 트럭 추가
        if queue and current_weight + queue[0] <= weight and len(bridge) < bridge_length:
            truck = queue.popleft()
            bridge.append((bridge_length, truck))
            current_weight += truck

    return answer


bridge_length_list = [2, 100, 100]
weight_list = [10, 100, 100]
truck_weights_list = [
    [7,4,5,6],
    [10],
    [10,10,10,10,10,10,10,10,10,10]
]
return_list = [8, 101, 110]
for br, we, tr in zip(bridge_length_list, weight_list, truck_weights_list):
    print(solution(br, we, tr))
