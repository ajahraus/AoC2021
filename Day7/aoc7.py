from functools import reduce
from pathlib import Path


def main():
    s = []
    with open(Path("aoc7-input.txt"), "r") as f:
        s = f.readlines()

    vals = [int(a) for a in s[0].strip().split(sep=',')]
    costs = [sum(abs(x-i)*(abs(x-i)+1)/2 for x in vals) for i in range(len(vals))]
    min_val = min(costs)

    print(f"{min_val:}")


if __name__ == '__main__':
    main()
