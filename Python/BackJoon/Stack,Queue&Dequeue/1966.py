from collections import deque

T = int(input())  # 테스트 케이스의 개수

for i in range(T):
    N, M = map(int, input().split())
    priority = deque()
    priority.extend(map(int, input().split()))

    wanted_docs = priority[M]  # 내가 언제 나오는지 궁금한 문서의 중요도
    num = 1
    while True:
        max_priority = max(priority)
        if priority[0] == max_priority:
            docs = priority.popleft()
            if docs == wanted_docs:
                print(num)
                break
            num += 1
        else:
            priority.rotate(-1)



