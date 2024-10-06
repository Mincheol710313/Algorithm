""" O(n) 정의를 만족 확인 """
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print(1 if c * n0 >= a1*n0+a0 and a1 <= c else 0)