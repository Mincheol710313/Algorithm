def func(command, answer, video_len):
    video_min, video_sec = video_len.split(":")
    video_time = int(video_min)*60 + int(video_sec)

    min, sec = answer.split(":")
    min = int(min)
    sec = int(sec)

    if command == "next":
        sec = sec + 10

        if sec >= 60:
            min = min + 1
            sec -= 60
        
        time = min*60 + sec

        if time >= video_time:
            return video_len

        answer = str(min).zfill(2)+":"+str(sec).zfill(2)

    elif command == "prev":
        sec = sec - 10

        if sec < 0:
            min = min - 1
            sec += 60

        time = min * 60 + sec
        if time < 0:
            return "00:00"
        
        answer = str(min).zfill(2)+":"+str(sec).zfill(2)

    return answer
        

def solution(video_len, pos, op_start, op_end, commands):
    answer = pos  # command 이전일 경우 현재 위치가 pos의 위치

    # 오프닝 건너뛰기 우선 처리
    if op_start <= answer <= op_end:
        answer = op_end
    
    # commands 처리
    for command in commands:
        answer = func(command, answer, video_len)

        # 오프닝 건너뛰기 우선 처리
        if op_start <= answer <= op_end:
            answer = op_end

    return answer


# 테스트 케이스
print(solution("34:33","13:00", "00:55","02:55",["next", "prev"]))
print(solution("10:55","00:05", "00:15","06:55",["prev", "next", "next"]))
print(solution("07:22","04:05", "00:15","04:07",["next"]))