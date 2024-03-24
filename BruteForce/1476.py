E, S, M = map(int, input().split())
year = 1
while True:
    if (year-1) % 15 + 1 == E and (year-1) % 28 + 1 == S and (year-1) % 19 + 1 == M:
        break
    else:
        year += 1
print(year)