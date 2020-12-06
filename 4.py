import re

with open("inputs/4.txt", "r") as f:
    test = f.read()[:-1]


def p4_p1(doc):
    pports = doc.split("\n\n")
    fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    fields2 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
    s = [re.split(" |\\n", x) for x in pports]
    tot = 0
    for pport in s:
        stuff = set([re.match("(\w+):.*", x).group(1) for x in pport if x != ""])
        tot += int(fields == stuff)
        tot += int(fields2 == stuff)
    return tot


def checks(s, field):
    search = re.match(".*{}:(\S+).*".format(field), re.sub("\n", " ", s))

    if search is None:
        return False
    search = search.group(1)
    if field == "byr":
        return int(search) >= 1920 and int(search) <= 2002
    elif field == "iyr":
        return int(search) >= 2010 and int(search) <= 2020
    elif field == "eyr":
        return int(search) >= 2020 and int(search) <= 2030
    elif field == "hgt":
        if "cm" in search:
            return int(search[:-2]) >= 150 and int(search[:-2]) <= 193
        elif "in" in search:
            return int(search[:-2]) >= 59 and int(search[:-2]) <= 76
        else:
            return False
    elif field == "hcl":
        return search[0] == "#" and search[1:].isalnum() and len(search) == 7
    elif field == "ecl":
        return search in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return search.isnumeric() and len(search) == 9
    elif field == "cid":
        return True
    raise Exception("Field {} not recognized".format(search))


def p4_p2(doc):
    pports = doc.split("\n\n")
    fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    tot = 0
    port = pports[0]
    for port in pports:
        tot += int(all([checks(port, field) for field in fields]))
    return tot


if __name__ == "__main__":
    print("Part 1: {}".format(p4_p1(test)))
    print("Part 2: {}".format(p4_p2(test)))
