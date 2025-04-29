# PCCP 1. 동영상 재생기
def solution(video_len, pos, op_start, op_end, commands):
    video_len_hour, video_len_minute = map(int, video_len.split(":"))
    video_len = video_len_hour * 60 + video_len_minute
    pos_hour, pos_minute = map(int, pos.split(":"))
    pos = pos_hour * 60 + pos_minute
    pos_hour, pos_minute = map(int, op_start.split(":"))
    op_start = pos_hour * 60 + pos_minute
    pos_hour, pos_minute = map(int, op_end.split(":"))
    op_end = pos_hour * 60 + pos_minute

    if op_start <= pos < op_end:
        pos = op_end

    for command in commands:
        if command == "next":
            pos += 10

            if video_len <= pos:
                pos = video_len
            elif op_start <= pos < op_end:
                pos = op_end
        else:
            pos -= 10
            if pos < 0:
                pos = 0
            if op_start <= pos < op_end:
                pos = op_end
    hour = format(pos //60,'02')
    minute = format(pos % 60,'02')
    return f"{hour}:{minute}"
