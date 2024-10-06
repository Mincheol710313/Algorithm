N, B = map(int, input().split())
num_list = []

while N != 0 and N != 1:
    remain = N % B
    if 10 <= remain <= 35:
        remain = chr(65 + remain - 10)
    num_list.append(remain)
    N = N // B
if N == 1:
    num_list.append(1)
num_list.reverse()

for num in num_list:
    print(num, end="")