from utils import load_input


def fst(lines):
    curr_ind = 0
    tot = 0
    for line in lines:
        tot += int(line[curr_ind % len(line)] == "#")
        curr_ind += 3
    return tot


def find_slope(lines, down, right):
    curr_ind = 0
    tot = 0
    for i in range(0, len(lines), down):
        tot += int(lines[i][curr_ind % len(lines[i])] == "#")
        curr_ind += right
    return tot


def snd(lines, instructions):
    tot = 1
    for ins in instructions:
        tot *= find_slope(lines, down=ins[1], right=ins[0])
    return tot


def main():
    test = load_input("3-test.txt")
    print("Part 1: {}".format(fst(test)))
    real = load_input("3.txt")
    print(
        "Part 2: {}".format(
            snd(real, instructions=[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
        )
    )


if __name__ == "__main__":
    main()
