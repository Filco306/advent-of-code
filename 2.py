from collections import Counter
from utils import load_input


def preprocess(lines):
    ls = []
    for line in lines:
        guide, text = line.split(":")
        min_num, snd = guide.split("-")
        min_num = int(min_num)
        max_num, letter = snd.split(" ")
        text = text.strip()
        ls.append((min_num, int(max_num), letter, text))
    return ls


def is_valid(tup):
    c = Counter(tup[3])
    return c[tup[2]] >= tup[0] and c[tup[2]] <= tup[1]


def p2_validity(tup):
    return (int(tup[3][tup[0] - 1] == tup[2]) + int(tup[3][tup[1] - 1] == tup[2])) == 1


def analyze_lines(a, preprocess_tup=True, p2=False):
    if preprocess_tup:
        vals = preprocess(a)
    else:
        vals = a
    tot = 0
    for val in vals:
        if p2 is False:
            tot += int(is_valid(val))
        else:
            tot += int(p2_validity(val))
    return tot


def main():
    a = """1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc""".split(
        "\n"
    )
    assert analyze_lines(a, p2=True) == 1
    b = load_input("2.txt").split("\n")
    print(analyze_lines(b, p2=True))


if __name__ == "__main__":
    main()
