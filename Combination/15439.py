N = int(input())

count = 0
for i in range(N):
    for j in range(N):
        if i != j:
            count += 1
print(count)