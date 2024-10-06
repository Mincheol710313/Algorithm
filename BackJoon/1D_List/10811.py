n, m = map(int, input().split())  # map 함수 기억하기
result = [i for i in range(1, n+1)]

for _ in range(m):
    first_idx, second_idx = map(int, input().split())
    reverse_list = list(reversed(result[first_idx-1:second_idx]))
    result[first_idx-1:second_idx] = reverse_list

for num in result:
    print(num, end=" ")
