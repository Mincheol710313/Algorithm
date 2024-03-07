words = list(input())
new_word = []

for i in range(len(words)):
    if words[i] == "c":
        if words[i+1] == "=":
            new_word.apped("c=")
        elif words[i+1] == "-":
            new_word.append("c-")
        else:
            new_word.append("c")
    elif words[i] == "d":
        if words[i+1] == "z":
            if words[i+2] == "=":
                new_word.append("dz=")
            else:
                new_word.append("d")
                new_word.append("z")
        elif words[i+1] == "-":
            new_word.append("d-")
        else:
            new_word.append("d")
    elif words[i] == "l":
        if words[i+1] == "j":
            new_word.append("lj")
        else:
            new_word.append("l")
    elif words[i] == "n":
        if words[i + 1] == "j":
            new_word.append("nj")
        else:
            new_word.append("n")
    elif words[i] == "s":
        if words[i + 1] == "=":
            new_word.append("s=")
        else:
            new_word.append("s")
    elif words[i] == "z":
        if words[i + 1] == "=":
            new_word.append("z=")
        else:
            new_word.append("z")
    else:
        new_word.append(words[i])

print(len(new_word))

