from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass
class BingoTile:
    number: int
    is_called: bool


@dataclass
class BingoCard:
    squares: List[BingoTile]

    def check_rows_and_cols(self):
        for i in range(5):
            if all(self.squares[(i * 5) + j] for j in range(5)) or all(self.squares[(j * 5) + i] for j in range(5)):
                self.winner()

    def winner(self):
        pass


def main():
    with open(Path("aoc4-input.txt"), "r") as f:
        s = f.readlines()

    [print(x) for x in s]
    bingo_calls = [int(x) for x in s[0].split(',')]

    print(bingo_calls)


if __name__ == '__main__':
    main()
