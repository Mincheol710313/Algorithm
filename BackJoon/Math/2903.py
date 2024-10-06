N = int(input())
dot_list = [0 for i in range(16)]
a = 2
b = 1

for i in range(1, 16):
    a += b
    dot_list[i] = pow(a, 2)
    b *= 2

print(dot_list[N])