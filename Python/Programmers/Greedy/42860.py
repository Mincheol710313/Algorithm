def solution(name):
    answer = 0

    len_name = len(name)

    first = 'A' * len_name

    diff = []
    diff_idxs = []
    present = 0
    pre = 0
    suf = 0

    for idx in range(len_name):
        d = ord(name[idx]) - ord(first[idx])
        if d > 12:
            d = abs(d - 25) + 1

        if d != 0:
            diff_idxs.append(idx)

            if idx <= len_name // 2:
                pre += 1
            else:
                suf += 1
   
        diff.append(d)
    
    answer += sum(diff)
    if 0 in diff_idxs:
        pre -= 1
        diff_idxs.remove(0)
    
    while len(diff_idxs) != 0:
        min_diffs = []
        for diff_idx in diff_idxs:
            if present < diff_idx:
                present_diff_idx = min(abs(present-diff_idx), abs(present+(len_name-diff_idx)))
            else:
                present_diff_idx = min(abs(present-diff_idx), abs((len_name-present) + diff_idx))

            min_diffs.append(present_diff_idx)
        
        min_diff = min(min_diffs)
        idxs = []
        for idx in range(len(diff_idxs)):
            if min_diffs[idx] == min_diff:
                idxs.append(idx)
        
        if len(idxs) == 1:
            idx = idxs[0]
            answer += min_diff
            present = diff_idxs[idx]
            diff_idxs.remove(present)
        else:
            if pre >= suf:
                idx = max(idxs)
                answer += min_diff
                present = diff_idxs[idx]
                diff_idxs.remove(present)
            else:
                idx = min(idxs)
                answer += min_diff
                present = diff_idxs[idx]
                diff_idxs.remove(present)
        
    return answer

# 테스트 케이스
print(solution("AAA"))
print(solution("AAB"))
print(solution("JAZ"))
print(solution("JAN"))
print(solution("JEROEN"))
print(solution("ABBAAABAAAABB"))
print(solution("BBBBAAAABA"))
