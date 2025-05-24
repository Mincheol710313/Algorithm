"""
인사성 밝은 곰곰이
새로운 사람이 입장(ENTER) 이후 "처음 채팅"을 입력하는 사람은 곰곰티콘으로 인사
그 외의 기록은 곰곰티콘을 쓰지않는 평범한 채팅 기록
채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!
"""
N = int(input())
chat_list = []
idx = -1
for _ in range(N):
    log = input()
    if log == "ENTER":
        chat_list.append(set())
        idx += 1
    else:
        chat_list[idx].add(log)
result = 0
for i in range(len(chat_list)):
    result += len(chat_list[i])
print(result)