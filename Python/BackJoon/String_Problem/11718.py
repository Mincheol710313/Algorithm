import sys
string_list = []
while True:
    string = sys.stdin.readline().strip()
    if not string:
        break
    string_list.append(string)

for string in string_list:
    print(string)