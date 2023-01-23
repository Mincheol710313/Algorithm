present = list(map(int, input().split()))
oven = int(input())

if (present[1] + oven >= 60):
    present[1] = present[1] + oven
    add_hour = int((present[1]) / 60)
    present[1] -= 60 * add_hour

    if present[0] + add_hour >= 24:
        present[0] = present[0] + add_hour - 24
    else:
        present[0] += add_hour
else:
    present[1] += oven

print(present[0], present[1])