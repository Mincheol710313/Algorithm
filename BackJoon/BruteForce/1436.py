N = int(input())

count = 0
num = 1
while True:
    num_str = str(num)
    if "666" in num_str:
        count += 1

    if count == N:
        print(num)
        break

    num += 1