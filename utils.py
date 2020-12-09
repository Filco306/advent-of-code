import os


def load_input(file_name):
    with open(os.path.join("inputs", file_name), "r") as f:
        ret = f.read()[:-1]
    return ret


def get_sum_of_2_nums(li, tot_sum=2020):
    d = set()
    for num in li:
        if num in d:
            return num * (tot_sum - num)
        d.add(tot_sum - num)
    return None


class FenwickTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)

        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self.update(i, nums[i])

    def update(self, i, value):
        i += 1
        while i <= self.n:
            self.tree[i] += value
            i += i & (-i)

    def get_sum_between(self, x2, x1):
        return self.get_sum(max(x1, x2)) - self.get_sum(min(x2, x1) - 1) * int(
            min(x1, x2) != 0
        )

    def get_sum(self, i):
        tot = 0
        i = i + 1
        while i > 0:
            tot += self.tree[i]

            i -= i & (-i)
        return tot
