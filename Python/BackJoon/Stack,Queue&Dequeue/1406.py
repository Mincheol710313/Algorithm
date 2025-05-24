sent = list(input()) + ["*"]  # 이미 Stack 상태로 생각
length = len(sent)
N = int(input())  # 주문의 수
idx = len(sent) - 1  # 커서의 위치
stack = []  # 결과

for i in range(N):
    order = list(input().split())

    if order[0] == "L":
        if idx == 0:
            continue
        else:
            for j in range(length):
                word = sent.pop()

                if word == '*':
                    left_word = sent.pop()
                    stack.append(left_word)
                    sent.append(word)
                    idx -= 1

                    for k in range(len(stack)):
                        sent.append(stack.pop())
                    break
                else:
                    stack.append(word)
    elif order[0] == "D":
        if idx == length - 1:
            continue
        else:
            for j in range(length):
                word = sent.pop()

                if word == '*':
                    right_word = stack.pop()
                    sent.append(right_word)
                    stack.append(word)
                    idx += 1

                    for k in range(len(stack)):
                        sent.append(stack.pop())
                    break
                else:
                    stack.append(word)
    elif order[0] == "B":
        if idx == 0:
            continue
        else:
            for j in range(length):
                word = sent.pop()

                if word == '*':
                    sent.pop()
                    stack.append(word)
                    idx -= 1
                    length -= 1

                    for k in range(len(stack)):
                        sent.append(stack.pop())
                    break
                else:
                    stack.append(word)
    elif order[0] == "P":
        add_word = order[1]

        for i in range(length):
            word = sent.pop()

            if word == '*':
                stack.append(word)
                sent.append(add_word)
                idx += 1
                length += 1

                for j in range(len(stack)):
                    sent.append(stack.pop())
                break
            else:
                stack.append(word)

for i in sent:
    if i != '*':
        print(i, end="")