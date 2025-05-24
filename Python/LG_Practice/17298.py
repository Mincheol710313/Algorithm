""" 오큰수 https://wikidocs.net/218200 """

n = int(input())
num_list = list(map(int, input().split()))

s = []
ans = [0] * n
for i in range(n):
    if len(s) == 0:
        s.append(i)
    
    while num_list[s[-1]] < num_list[i]:
        ans[s.pop()] = num_list[i]

        if len(s) == 0:
            break
    
    s.append(i)

if len(s) != 0:
    for i in s:
        ans[i] = -1

for num in ans:
    print(num, end=" ")