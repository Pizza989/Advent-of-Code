with open("input.txt", "r") as file:
    elves_calories = [
        sum(map(int, block.split("\n")))
        for block in "".join(file.readlines()).split("\n\n")
    ]

    print(max(elves_calories))  # Part 1
    print(sum(sorted(elves_calories)[-3:]))  # Part 2
