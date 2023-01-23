import math

A, B, V = map(int, input().split())

#  +1은 마지막에 올라가야하기 때문에 그 하루를 의미
day = math.ceil((V - A) / (A - B)) + 1

print(day)