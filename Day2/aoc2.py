from dataclasses import dataclass
from pathlib import Path


@dataclass
class DirectionDistance:
    direction: str
    distance: int


def main():
    s = []
    with open(Path("aoc2-input.txt"), "r") as f:
        s = f.readlines()
    separated = [a.strip().split(sep=" ") for a in s]

    inputs = [DirectionDistance(direction=sep[0], distance=int(sep[1])) for sep in separated]
    for i in inputs:
        i.distance = int(i.distance)
    [print(a) for a in inputs]
    h_pos = 0
    depth = 0
    aim = 0
    for i in inputs:
        match i:
            case DirectionDistance(direction="forward"):
                h_pos += i.distance
                depth += (i.distance * aim)
            case DirectionDistance(direction="down"):
                aim += i.distance
            case DirectionDistance(direction="up"):
                aim -= i.distance
    print(f"{h_pos=}, {depth=}, {h_pos*depth=}")


if __name__ == '__main__':
    main()