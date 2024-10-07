from itertools import combinations

def solution(clothes):
    answer = 0

    clothes_hash = {}

    for clothe in clothes:
        _, key = clothe[0], clothe[1]

        if key not in clothes_hash.keys():
            clothes_hash[key] = 1
        else:
            clothes_hash[key] += 1

    key_len = len(clothes_hash.keys())

    for lenght in range(1,key_len + 1):
        for clothe_keys in combinations(clothes_hash.keys(), lenght):
            count = 1
            for key in clothe_keys:
                count *= clothes_hash.get(key)
            answer += count

    return answer

# 테스트 케이스
print(solution([["yellow_hat", "headgear"]]))
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))