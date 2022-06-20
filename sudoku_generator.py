from sudoku import Sudoku
from sudoku_solver import SudokuSolver


class SudokuGenerator:
    def __init__(self):
        self.g = Sudoku()
        self.s = SudokuSolver()
        self.solution = ''

    def get_sudoku(self):
        sg = SudokuGenerator()
        self.g.generate_board()
        board = self.g.get_partial_sudoku_matrix()
        self.s.solve_sudoku(board)
        if str(self.s) == str(self.g):
            self.g.print_grid()
            self.solution += self.s.solution
            print(self.solution)
        else:
            sg.get_sudoku()

    def print_solution(self):
        print(self.s)
        print(self.g)

    def __str__(self):
        return self.solution



