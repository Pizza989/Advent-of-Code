post_struct = [[] for i in range(9)]


def parse_input():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        pre_struct, cmds = "".join(lines).split("\n\n")
        cmds = [cmd.split() for cmd in cmds.splitlines()]
        pre_struct = [
            pre_struct[i : i + 4].strip() for i in range(0, len(pre_struct), 4)
        ]

        for i in range(0, len(pre_struct), int(pre_struct[-1])):
            for j in range(9):
                _ = pre_struct[i + j].replace("[", "").replace("]", "")
                post_struct[j].append(_) if _ and not _.isdigit() else None

    return cmds, post_struct


def part1(cmds, post_struct):
    for cmd in cmds:
        for i in range(int(cmd[1])):
            post_struct[int(cmd[5]) - 1].insert(
                0, post_struct[int(cmd[3]) - 1].pop(0)
            )

    return "".join([sub[0] for sub in post_struct])


def part2(cmds, post_struct):
    for cmd in cmds:
        for each in reversed(
            [post_struct[int(cmd[3]) - 1].pop(0) for i in range(int(cmd[1]))]
        ):
            post_struct[int(cmd[5]) - 1].insert(0, each)

    return "".join([sub[0] for sub in post_struct])


if __name__ == "__main__":
    print(part2(*parse_input()))
