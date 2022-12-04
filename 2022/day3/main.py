import string


with open("input.txt", "r") as file:
    res = []
    for line in file.readlines():
        length = len(line)
        a, b = line[: length // 2], line[length // 2 :]

        for char in a:
            if char in b:
                res.append(char)
                break

print(sum(map(lambda x: string.ascii_letters.index(x) + 1, res)))

with open("input.txt", "r") as file:
    pass
