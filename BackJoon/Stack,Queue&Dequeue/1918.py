import sys

stack = []  # 피연산자 Stack
result = ''  # 후위 표기법 eqn

eqn = list(sys.stdin.readline().rstrip())  # 중위 표기식으로 들어오는 eqn
for com in eqn:
    if com.isalpha():
        result += com
    else:
        if com == '(':
            stack.append(com)
        elif com == '*' or com == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(com)
        elif com == '+' or com =='-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(com)
        elif com == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)