N = int(input())  # 출입 기록의 수

enter_log = {}

for _ in range(N):
    name, status = map(str, input().split())
    enter_log[name] = status

left_list = []
for name, status in enter_log.items():
    if status == 'enter':
        left_list.append(name)

left_list.sort(reverse=True)
for name in left_list:
    print(name)