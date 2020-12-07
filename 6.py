from utils import load_input


def split(word):
    return [char for char in word]


def p1(s):
    a = s.split("\n\n")
    tot = 0
    for group in a:
        tot += len(set([x for x in group if x != "\n"]))
    return tot


def p2(s):
    tot = 0
    for group in s.split("\n\n"):
        ppls = group.split("\n")
        setlist = []
        for ppl in ppls:
            if ppl != "":
                setlist.append(set(split(ppl)))
        tot += len(setlist[0].intersection(*setlist))
    return tot


def main():
    test = load_input("6-test.txt")
    assert p1(test) == 11
    a = load_input("6.txt")
    print("Part 1 : {}".format(p1(a)))
    assert p2(test) == 6
    print("Part 2 : {}".format(p2(a)))


if __name__ == "__main__":
    main()
