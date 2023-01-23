def han(N):
    def seq(num):
        digits = list(map(int, str(num)))
        if len(digits) == 1:
            return True

        d = digits[1] - digits[0]
        i = 0
        while digits[i] + d == digits[i + 1]:
            i += 1
            if i == len(digits) - 1:
                return True

        return False

    N = int(N)
    han_num = []
    for n in range(1, N + 1):
        if seq(n):
            han_num.append(n)
    return len(han_num)


N = int(input())
print(han(N))