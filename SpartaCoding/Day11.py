N, M = map(int, input().split()) # N : Node 개수, M : 간선 개수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())

    graph[x].append(y)

S = int(input())
gomgom_list = list(map(int, input().split()))

s = []
s.append(1)
flag = True
while s:
    v = s.pop()

    if v in gomgom_list:
        continue
    else:
        if len(graph[v]) == 0:
            flag = False 
        for idx in graph[v]:
            s.append(idx)

if flag:
    print("Yes")
else:
    print("yes")