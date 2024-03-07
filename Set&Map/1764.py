N, M = map(int, input().split())

no_listen_set = set()
no_see_set = set()

for _ in range(N):
    name = input()
    no_listen_set.add(name)

for _ in range(M):
    name = input()
    no_see_set.add(name)

no_listen_see_set = no_listen_set & no_see_set
no_listen_see_list = sorted(list(no_listen_see_set))
print(len(no_listen_see_set))
for name in no_listen_see_list:
    print(name)