def solution(clothes):
    answer = 1

    clothes_hash = {}

    for clothe in clothes:
        _, key = clothe[0], clothe[1]

        if key not in clothes_hash.keys():
            clothes_hash[key] = 1
        else:
            clothes_hash[key] += 1

    for val in clothes_hash.values():
        answer *= (val + 1)

    return answer-1

# 테스트 케이스
print(solution([["yellow_hat", "headgear"]]))
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))