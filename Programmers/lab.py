clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

clothe_hash = {}

for clothe in clothes:
    val, key = clothe[0], clothe[1]

    if key not in clothe_hash.keys():
        clothe_hash[key] = [val]
    else:
        clothe_hash[key].append(val)

print(len(clothe_hash.keys()))