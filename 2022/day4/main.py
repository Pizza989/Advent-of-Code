def contains(r1, r2):
    return (
        r1[0] <= r2[0] and r1[1] >= r2[1] or r2[0] <= r1[0] and r2[1] >= r1[1]
    )


def overlap(r1, r2):
    return range(max(r1[0], r2[0]), min(r1[1] + 1, r2[1] + 1))


with open("input.txt", "r") as file:
    c = 0
    d = 0
    for line in file.readlines():
        split = line.split(",")
        r1, r2 = list(map(int, split[0].split("-"))), list(
            map(int, split[1].split("-"))
        )
        c += 1 if contains(r1, r2) else 0
        d += 1 if overlap(r1, r2) else 0

    print(c)
    print(d)
