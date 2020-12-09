from utils import load_input, get_sum_of_2_nums, FenwickTree


def p1(s, jump):
    s = [int(x) for x in s.split("\n")]
    for i in range(jump, len(s)):
        if get_sum_of_2_nums(s[i - jump : i], tot_sum=s[i]) is None:  # noqa: E203
            return s[i]
    raise Exception("All numbers have a sum here. ")


def p2_old(s, num):
    # Deprecated. Not as fast.
    # Good if numbers are changing
    s = [int(x) for x in s.split("\n")]
    ftree = FenwickTree(s)
    for i in range(0, len(s) - 1):
        for j in range(i + 1, len(s)):
            if ftree.get_sum_between(i, j) == num:
                return max(s[i : (j + 1)]) + min(s[i : (j + 1)])  # noqa: E203


def p2(s, num):
    s = [int(x) for x in s.split("\n")]

    for i in range(0, len(s) - 1):
        fst = i
        last = -1
        tot = sum(s[fst : (last + 1)])  # noqa: E203
        for j in range(i + 1, len(s)):
            if (i == 0 and j == 1) is False:
                if i != fst:
                    tot -= s[fst]
                    fst = i
                if j != last:
                    tot += s[j]
                    last = j
                if tot == num:
                    return max(s[fst : (last + 1)]) + min(  # noqa: E203
                        s[fst : (last + 1)]  # noqa: E203
                    )


def main():
    test = load_input("9-test.txt")
    real = load_input("9.txt")
    assert p1(test, jump=5) == 127
    print("Part 1 : {}".format(p1(real, jump=25)))
    assert p2(test, p1(test, jump=5)) == 62
    print("Part 2 : {}".format(p2(real, p1(real, jump=25))))


if __name__ == "__main__":
    main()
