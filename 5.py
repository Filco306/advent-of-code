def convert(s="FBFBBFF", one="B", zero="F"):
    return int("".join(["1" if x == one else "0" for x in s]), 2)


def p1(s="FBFBBFFRLR"):
    row = s[:7]
    col = s[7:]
    return convert(s=row) * 8 + convert(s=col, one="R", zero="L")


if __name__ == "__main__":
    assert p1("FBFBBFFRLR") == 357
    assert p1("BFFFBBFRRR") == 567
    assert p1("FFFBBBFRRR") == 119
    assert p1("BBFFBBFRLL") == 820
    with open("inputs/5.txt", "r") as f:
        a = f.read().split("\n")[:-1]
    print("Part 1 : {}".format(max([p1(x) for x in a])))

    # part 2
    all_seats = set([p1(x) for x in a])
    for seat in range(min(all_seats), max(all_seats)):
        if seat not in all_seats:
            ans = seat
            break
    print("Part 2 : {}".format(ans))
