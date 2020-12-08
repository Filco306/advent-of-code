from utils import load_input
from copy import deepcopy


class Interpreter:
    def __init__(self):
        self.accumulator = 0

    def process(self, ins):
        instructions = []
        for line in ins:
            instruc, num = line.split(" ")
            instructions.append((instruc, int(num)))
        return instructions

    def interpret_instruction(self, ins, num):
        if ins == "acc":
            self.accumulator += num
            step = 1
        elif ins == "nop":
            step = 1
        elif ins == "jmp":
            step = num
        return step

    def operate(self, instructions, process=True):
        if process is True:
            instructions = self.process(instructions)
        self.accumulator = 0
        i = 0
        done = False
        self.used = set()

        while done is False:
            # print(i)
            self.used.add(i)
            step = self.interpret_instruction(instructions[i][0], instructions[i][1])
            i += step
            if i in self.used or i >= len(instructions):
                done = True
        terminated_correctly = i >= len(instructions)
        return self.accumulator, step, terminated_correctly


def p2(ins, inter):
    ins = inter.process(ins)
    nops_jmps = []
    for i, tup in enumerate(ins):
        if tup[0] in ["nop", "jmp"]:
            nops_jmps.append(i)

    for i in nops_jmps:
        candidate = deepcopy(ins)
        if candidate[i][0] == "nop":
            candidate[i] = ("jmp", candidate[i][1])
        else:
            candidate[i] = ("nop", candidate[i][1])
        accumulator, step, terminated_correctly = inter.operate(
            candidate, process=False
        )
        if terminated_correctly is True:
            return accumulator
    raise Exception("No change fixed the problem! ")


def main():
    test = load_input("8-test.txt").split("\n")
    inter = Interpreter()
    assert inter.operate(test)[0] == 5
    real = load_input("8.txt").split("\n")
    print("Part 1 : {}".format(inter.operate(real)[0]))
    assert p2(test, inter) == 8
    print("Part 2 : {}".format(p2(real, inter)))


if __name__ == "__main__":
    main()
