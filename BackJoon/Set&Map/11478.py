"""
서로 다른 부분 문자열의 개수
부분 문자열 기준 : 문자열 S에서 "연속된" 일부분, 길이가 1보다 크거나 같다.
"""
string = input()
string_set = set()
for i in range(0, len(string)):
    for j in range(i+1, len(string)+1):
        substring = string[i:j]
        string_set.add(substring)
print(len(string_set))
