string = input()
reverse_string = list(reversed(string))

result = 1
for i in range(len(string)):
    if string[i] != reverse_string[i]:
        result = 0

print(result)
