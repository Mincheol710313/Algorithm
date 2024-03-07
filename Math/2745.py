num, base = map(str, input().split())
base = int(base)

result = 0
for idx in range(len(num)):
    if 'A' <= num[idx] <= 'Z':
        result += pow(base, len(num)-1-idx)*(ord(num[idx])-65+10)
    else:
        result += pow(base, len(num)-1-idx)*int(num[idx])

print(result)
