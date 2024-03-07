x, y, w, h = map(int, input().split())

result = x
if abs(x-w) < result:
    result = abs(x-w)

if y < result:
    result = y

if abs(y-h) < result:
    result = abs(y-h)

print(result)