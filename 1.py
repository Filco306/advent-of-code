from itertools import combinations
from utils import get_sum_of_2_nums


def get_ans_2(li, tot_sum=2020):
    d = {}
    for i, num1 in enumerate(li):
        d[tot_sum - num1] = i
    for i, j in combinations(range(len(li)), 2):
        num1 = li[i]
        num2 = li[j]
        if num1 + num2 in d and d[num1 + num2] not in (i, j):
            return num1 * num2 * li[d[num1 + num2]]
    raise Exception("ERROR NO 3 NUMBERS SUM UP TO {} IN LIST".format(tot_sum))


def main():
    with open("inputs/1.txt", "r") as f:
        a = [int(x) for x in f.read().split("\n")[:-1]]
    test = [1721, 979, 366, 299, 675, 1456]
    assert get_sum_of_2_nums(test) == 514579
    print("Ans part 1: {}".format(get_sum_of_2_nums(a)))

    assert get_ans_2(test) == 241861950
    print("Ans part 2: {}".format(get_ans_2(a)))


if __name__ == "__main__":
    main()
