# 동영상 재생기

def solution(video_len, pos, op_start, op_end, commands):
    arr = []    # 비디오 길이, 오프닝 시작, 오프닝 끝
    current = 60 * int(pos.split(":")[0]) + int(pos.split(":")[1])

    for time in [video_len, op_start, op_end]:
        m, s = map(int, time.split(":"))
        arr.append(m*60+s)

    for c in [""]+commands:
        # 명령에 따라 현재 위치 이동
        if c == "prev":
            current -= 10
        elif c == "next":
            current += 10

        # 동영상 범위 벗어나는 경우 영상의 처음 혹은 끝으로 이동
        if current < 0:
            current = 0
        if current > arr[0]:
            current = arr[0]

        # 현재 위치가 오프닝 범위일 경우 오프닝 끝으로 이동
        if arr[1] <= current < arr[2]:
            current = arr[2]

    mm = "{:02d}".format(current // 60)
    ss = "{:02d}".format(current % 60)
    return f'{mm}:{ss}'


video_len_list = ["34:33", "10:55", "07:22", "10:00"]
pos_list = ["13:00", "00:05", "04:05", "00:03"]
op_start_list = ["00:55", "00:15", "00:15", "00:00"]
op_end_list = ["02:55", "06:55", "04:07", "00:05"]
commands_list = [
    ["next", "prev"],
    ["prev", "next", "next"],
    ["next"],
    ["prev", "next"]
]

for video, pos, start, end, command in zip(video_len_list, pos_list, op_start_list, op_end_list, commands_list):
    print(solution(video, pos, start, end, command))
