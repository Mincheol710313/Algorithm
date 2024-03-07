while True:
    sent = input()

    if sent == '.':
        break

    stack = []
    Ans = "yes"
    for Par in sent:
        if (Par == '(') or (Par == '['):
            stack.append(Par)
        elif Par == ')':
            if len(stack) == 0:
                Ans = "no"
                break
            elif stack.pop() != '(':
                Ans = "no"
                break
        elif Par == ']':
            if len(stack) == 0:
                Ans = "no"
                break
            elif stack.pop() != '[':
                Ans = "no"
                break

    if Ans == "yes":
        if len(stack) != 0:
            print("no")
        else:
            print("yes")
    else:
        print("no")

