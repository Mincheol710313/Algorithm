def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    length = len(sorted_phone_book)
    
    for idx in range(length-1):
        prefix = sorted_phone_book[idx]
        prefix_len = len(prefix)

        if prefix_len <= len(sorted_phone_book[idx+1]) and prefix == sorted_phone_book[idx+1][:prefix_len]:
            return False

    return True

# 테스트 케이스
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))