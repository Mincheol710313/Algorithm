# from math import factorial
# print(factorial(int(input())))

def facto(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * facto(N-1)

print(facto(int(input())))