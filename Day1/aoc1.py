from pathlib import Path
from typing import List, Optional


def get_set_of_three_index(s: List[int]) -> List[int]:
    return [sum(s[i-1:i+2]) for i in range(1, len(s)-1)]


def main():
    s = []
    with open(Path("aoc1-input.txt"), "r") as f:
        s = f.readlines()
        s = [int(s.strip()) for s in s]
    mean_depths = get_set_of_three_index(s)
    [print(i) for i in mean_depths]
    d = sum([1 if mean_depths[i-1] < mean_depths[i] else 0 for i in range(1, len(mean_depths))])
    print(d)



if __name__ == "__main__":
    main()
