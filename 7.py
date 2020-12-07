from utils import load_input
import re


# Copied from Rocku0@Grepper
class My_stack:
    def __init__(self):
        self.data = []

    def my_push(self, x):
        return self.data.append(x)

    def my_pop(self):
        return self.data.pop()

    def my_peak(self):
        return self.data[-1]

    def my_contains(self, x):
        return self.data.count(x)

    def my_show_all(self):
        return self.data

    def empty(self):
        return len(self.data) == 0


def convert_desc(bag_desc):
    ret = re.sub("\d+ ", "", bag_desc)
    if "." == ret[-1]:
        ret = ret[:-1]
    if "s" == ret[-1]:
        return ret[:-1]
    return ret


def p1(s):
    parents = {}
    a = s.split("\n")
    for line in a:
        bag, content = line.split(" contain ")
        contents = content.split(", ")
        for content in contents:
            if convert_desc(content) not in parents:
                parents[convert_desc(content)] = set()
            parents[convert_desc(content)].add(convert_desc(bag))
    stack = My_stack()
    all_bags = set()

    for parent in parents["shiny gold bag"]:
        stack.my_push(parent)
        all_bags.add(parent)

    while stack.empty() is False:
        curr_bag = stack.my_pop()
        all_bags.add(curr_bag)
        if curr_bag in parents:
            for parent in parents[curr_bag]:
                stack.my_push(parent)
    return len(all_bags)


def p2_recursive(curr, curr_parents, parents, curr_bag):
    tot = 0
    for parent in curr_parents:
        tot += parent[0] * curr
        if parent[1] in parents:
            tot += p2_recursive(
                curr * parent[0], parents[parent[1]], parents, curr_bag=parent[1]
            )
    return tot


def p2(s):
    parents = {}
    children = {}
    a = s.split("\n")
    for line in a:
        bag, content = line.split(" contain ")
        contents = content.split(", ")
        children[convert_desc(bag)] = set()
        for content in contents:
            if "no other bags" not in content:
                children[convert_desc(bag)].add(
                    (int(re.match("(\d+)", content).group(1)), convert_desc(content))
                )
            if convert_desc(content) not in parents:
                parents[convert_desc(content)] = set()
            if "no other bags" not in content:
                parents[convert_desc(content)].add(
                    (int(re.match("(\d+)", content).group(1)), convert_desc(bag))
                )
            else:
                parents[convert_desc(content)].add((0, convert_desc(bag)))
    return p2_recursive(1, children["shiny gold bag"], children, "shiny gold bag")


def main():
    test1 = load_input("7-test-1.txt")
    test2 = load_input("7-test-2.txt")
    assert p1(test1) == 4
    assert p2(test1) == 32
    assert p2(test2) == 126

    real = load_input("7.txt")

    print("Part 1: {}".format(p1(real)))
    print("Part 2: {}".format(p2(real)))


if __name__ == "__main__":
    main()
