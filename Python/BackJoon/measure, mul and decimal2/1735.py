import sys

def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)


def LCM(A, B, gcd):
    return int(A * B / gcd)

fraction1 = list(map(int, sys.stdin.readline().split()))
fraction2 = list(map(int, sys.stdin.readline().split()))

gcd = 0
if fraction1[1] > fraction2[1]:
    gcd = GCD(fraction1[1], fraction2[1])
else:
    gcd = GCD(fraction2[1], fraction1[1])
lcm = LCM(fraction1[1], fraction2[1], gcd)

fraction1_mul = int(lcm / fraction1[1])
fraction2_mul = int(lcm / fraction2[1])

fraction1[0] *= fraction1_mul
fraction2[0] *= fraction2_mul
fraction1[1] = lcm
fraction2[1] = lcm

num = fraction1[0] + fraction2[0]
demo = lcm

if num > demo:
    gcd = GCD(num, demo)
else:
    gcd = GCD(demo, num)

print(num//gcd, demo//gcd)