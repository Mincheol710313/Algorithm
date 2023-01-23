def fib(n):
    global fib_counter
    if n == 1 or n == 2:
        return 1
    else:
        fib_counter += 1
        return fib(n - 2) + fib(n - 1)


# Top - down 방식의 Dynamic Programing
n = int(input())

fib_array = [0] * 41
fib_array[1] = 1
fib_array[2] = 1
fibonacci_counter = 0

for i in range(3, n+1):
    fibonacci_counter += 1
    fib_array[i] = fibonacci_counter


fib_counter = 0
fib(n)
print(fib_counter, fib_array[n])
