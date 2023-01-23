T = int(input())  # 테스트 케이스의 개수

for i in range(T):
    sent = list(input())

    stack = []
    Ans = "YES"
    for Par in sent:
        if Par == '(':
            stack.append(Par)
        else:
            if len(stack) == 0:
                Ans = "NO"
                break
            else:
                stack.pop()

    if Ans == "YES":
        if len(stack) != 0:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")

