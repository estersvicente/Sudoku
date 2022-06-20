from random import sample
import numpy as np
# To use random sample numbers to create the sudoku board


class Sudoku:
    """
    Creates randomized sudoku boards (9x9) and outputs them in grid form
    """
    BASE = 3
    SIDE = BASE * BASE

    def __init__(self):
        self.board = []
        self.partial_board = []
        self.solution = []
        self.side = Sudoku.BASE * Sudoku.BASE
        self.num_size = len(str(self.side))

    def pattern(self, r, c):
        pattern = (Sudoku.BASE * (r % Sudoku.BASE) + r // Sudoku.BASE + c) % self.side
        if self:
            return pattern

    @staticmethod
    def shuffle(s):
        """
        Shuffles an input list s
        :param s: a list of numbers
        :return: a list of same size as the input list but with the numbers in a random order
        """
        return sample(s, len(s))

    @staticmethod
    def expand_line(line):
        return line[0] + line[5:9].join([line[1:5] * (Sudoku.BASE - 1)] * Sudoku.BASE) + line[9:13]

    def generate_board(self):
        """
        Generates a random board of sudoku that has only 1/4 of its numbers shown to the user
        (this creates a board of difficulty easy)
        :return: A incomplete sudoku board in matrix form (with 0 for the spaces that need to be completed)
        """
        base = range(Sudoku.BASE)
        rows = [g * Sudoku.BASE + r for g in Sudoku.shuffle(base) for r in Sudoku.shuffle(base)]
        cols = [g * Sudoku.BASE + c for g in Sudoku.shuffle(base) for c in Sudoku.shuffle(base)]
        nums = Sudoku.shuffle(range(1, Sudoku.BASE * Sudoku.BASE + 1))
        self.board = [[nums[Sudoku.pattern(self, r, c)] for c in cols] for r in rows]
        self.solution = np.copy(self.board)
        squares = self.side * self.side
        empties = squares * 51 // 81
        for p in sample(range(squares), empties):
            self.board[p // self.side][p % self.side] = 0
        self.partial_board = np.copy(self.board)

    def print_grid(self):
        line0 = Sudoku.expand_line("╔═══╤═══╦═══╗")
        line1 = Sudoku.expand_line("║ . │ . ║ . ║")
        line2 = Sudoku.expand_line("╟───┼───╫───╢")
        line3 = Sudoku.expand_line("╠═══╪═══╬═══╣")
        line4 = Sudoku.expand_line("╚═══╧═══╩═══╝")

        symbol = " 1234567890"
        nums = [[""] + [symbol[n] for n in row] for row in self.board]
        print(line0)
        for r in range(1, self.side + 1):
            print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
            print([line2, line3, line4][(r % self.side == 0) + (r % Sudoku.BASE == 0)])

    def get_partial_sudoku_matrix(self):
        return self.partial_board

    def __str__(self):
        s = ''
        for line in self.solution:
            s += str(line) + '\n'
        return s
