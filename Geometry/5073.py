while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    # 총 길이
    total_length = a + b + c

    # python 삼항 연산자 활용
    max_length = a if a > b else b
    max_length = c if c > max_length else max_length

    if (total_length-max_length) <= max_length:
        print("Invalid")
    else:
        if a == b and b ==c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")