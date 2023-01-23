number = int(input())
num_array = list(map(int, input().split()))
v = int(input())

same = 0
for i in range(number):
    if v == num_array[i]:
        same += 1

print(same)