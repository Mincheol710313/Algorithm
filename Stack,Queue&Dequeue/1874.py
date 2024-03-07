# 참고자료 : https://hongcoding.tistory.com/39

n = int(input())
s = []  # 스택
ans = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:
        s.append(cur)
        ans.append("+")
        cur += 1

    if s[-1] == num:
        s.pop()
        ans.append("-")
    else:
        print("NO")
        flag = -1
        break

if flag == 0:
    for i in ans:
        print(i)

