N = int(input())

words = []
for i in range(N):
    words.append(input())

words.sort(key=lambda x: (len(x), x))

present = 0
before = 0
for i in range(N):
    if present == 0:
        print(words[present])
        present += 1
    else:
        if words[present] == words[before]:
            present += 1
            before += 1
        else:
            print(words[present])
            present += 1
            before += 1