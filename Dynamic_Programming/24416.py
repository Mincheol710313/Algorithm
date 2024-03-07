import sys
recursion_n = 0
def fib(n):
    global recursion_n
    if n == 1 or n == 2:
        recursion_n += 1
        return 1  # 코드 1
    else:
        return fib(n-1) + fib((n-2))

def dynamic_fibo(n, fibo_list):
    count = 0
    for i in range(3, n+1):
        fibo_list[n] = fibo_list[n-1] + fibo_list[n-2]  # 코드 2
        count += 1
    return fibo_list[n], count

fibo_list = [0 for i in range(41)]
# 기저 상태 파악
fibo_list[1] = 1
fibo_list[2] = 1

n = int(sys.stdin.readline().rstrip())

# dp를 이용한 풀이
fib(n)
result, dynamic_n = dynamic_fibo(n, fibo_list)
print(recursion_n, dynamic_n)