from pathlib import Path


def main():
    with open(Path("aoc3-input.txt"), "r") as f:
        s = f.readlines()
    s = [a.strip() for a in s]
    result = [i for i in range(len(s[0]))]
    for i in range(len(s[0])):
        result[i] = sum([1 if a[i] == "1" else 0 for a in s])
    result_reduced = [a / len(s) for a in result]

    result_as_r = ["1" if r > 0.5 else "0" for r in result_reduced]
    filter_set = result[:]
    for i in range(len(result_as_r)):
        filter_set = [x for x in filter_set if x[i] == filter_set[i]]
    # result_as_r = result_as_r[::-1]
    not_r = ["1" if r == "0" else "0" for r in result_as_r]


    a = int("".join(result_as_r), 2)
    b = int("".join(not_r), 2)
    print(f"{a=}, {b=}, {a*b=}")


if __name__ == '__main__':
    main()
