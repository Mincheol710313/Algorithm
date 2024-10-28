X, Y = map(int, input().split())
Z = Y * 100 //X 

start = 0
end = X
ans = X

if (Z >= 99):
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2

        n_Z = (Y + mid) * 100 // (X + mid)

        if n_Z > Z:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
        
    print(ans)