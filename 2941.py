import sys

words = sys.stdin.readline()
word = []

num = 0
for i in words:
    if i in ['c', 'd', 'l', 'n', 's', 'z']:
        pass
    else:
        num += 1

