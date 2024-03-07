import sys
string_list = []
while True:
    string = sys.stdin.readline().strip()
    if not string:
        break
    string_list.append(string)

max_str_length = 0
for string in string_list:
    if max_str_length < len(string):
        max_str_length = len(string)

for char_idx in range(max_str_length):
    for string in string_list:
        if char_idx > len(string)-1:
            continue
        else:
            print(string[char_idx], end="")