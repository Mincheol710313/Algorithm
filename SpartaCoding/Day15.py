from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())

    ch_list = list(input().split())

    q = deque()
    q.append(ch_list[0])

    for idx in range(1, N):
        if ord(q[0]) >= ord(ch_list[idx]):
            q.appendleft(ch_list[idx])
        else:
            q.append(ch_list[idx])

    print(str(''.join(list(q))))