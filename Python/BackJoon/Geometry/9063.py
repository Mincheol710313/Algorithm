N = int(input())
result = 0

if N == 1:
    print(result)
else:
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    for i in range(N):
        if i == 0:
            x_min, y_min = map(int, input().split())
            x_max, y_max = x_min, y_min
        else:
            x, y = map(int, input().split())
            if x > x_max:
                x_max = x
            elif x < x_min:
                x_min = x

            if y > y_max:
                y_max = y
            elif y < y_min:
                y_min = y

result = (x_max - x_min) * (y_max - y_min)
print(result)