assignment = {
    "X": 1,  # rock
    "A": 1,
    "Y": 2,  # paper
    "B": 2,
    "Z": 3,  # scissors
    "C": 3,
}

scheme = ["A", "B", "C"]


def evaluate(a: str, b: str):
    a, b = assignment[a], assignment[b]
    if a == b:
        return b + 3

    match a:
        case 1:
            if b == 2:
                return b + 6
            elif b == 3:
                return b
        case 2:
            if b == 1:
                return b
            elif b == 3:
                return b + 6
        case 3:
            if b == 1:
                return b + 6
            elif b == 2:
                return b


with open("input.txt", "r") as file:  # part 1
    lines = file.readlines()

print(sum([evaluate(*line.split()) for line in lines]))


# part 2
new = []
for line in lines:
    a, b = line.split()
    match b:
        case "X":
            new.append(f"{a} {scheme[(scheme.index(a) - 1) % 3]}")
        case "Y":
            new.append(f"{a} {a}")
        case "Z":
            new.append(f"{a} {scheme[(scheme.index(a) + 1) % 3]}")

print(new)
print(sum([evaluate(*line.split()) for line in new]))
