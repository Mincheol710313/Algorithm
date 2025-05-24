def solution(brown, yellow):
    answer = []
    
    total = brown + yellow # 타일의 개수

    col = 3 # 열은 무조건 3개 이상 존재
    row =  total // col
   
    while True:
        if col < row:
            col += 1
            row = total // col
            continue
        else:
            if col * row - (col-2) * (row - 2) == brown and (col-2) * (row-2) == yellow:
                break
            else:
                col += 1
                row = total // col
    
    answer = [col, row]

    return answer

# 테스트 케이스
print(solution(10,2))
print(solution(8,1))
print(solution(24,24))