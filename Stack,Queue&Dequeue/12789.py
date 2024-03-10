"""
모든 사람들이 순서대로 간식을 받을 수 있는지 확인
"""
stack = []

N = int(input())  # 승환이 앞에 있는 학생들의 수
num_list = list(map(int, input().split()))  # 승환이 앞에 있는 학생들의 번호표
result = []

# Process #
for num in num_list:
    if len(stack) == 0:
        stack.append(num)
    else:
        while stack and (stack[-1] < num):  # stack이 비어있지 않고 stack의 맨 윗 요소보다 nu이 클 경우 그 stack의 요소 내보내기
            result.append(stack.pop())
        stack.append(num)

# stack 처리 한 후 모두 빼기 #
while stack:
    result.append(stack.pop())

# Nice 판단
nice = [i for i in range(1,N+1)]

if nice == result:
    print("Nice")
else:
    print("Sad")

