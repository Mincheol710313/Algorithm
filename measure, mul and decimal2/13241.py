import sys


def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)


def LCM(A, B, gcd):
    return int(A * B / gcd)


A, B = map(int, sys.stdin.readline().split())

gcd = 0
if A > B:
    gcd = GCD(A, B)
else:
    gcd = GCD(B, A)
lcm = LCM(A,B, gcd)
print(lcm)