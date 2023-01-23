# 재귀함수 호출 횟수 체크하는 방법
def recursion(s, l, r):
    recursion.counter += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


T = int(input())
words_list = []
for i in range(T):
    words_list.append(input())


for i in range(T):
    recursion.counter = 0
    print(isPalindrome(words_list[i]), recursion.counter)
