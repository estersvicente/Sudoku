from sudoku import Sudoku
from sudoku_solver import SudokuSolver


class SudokuGenerator:
    def __init__(self):
        self.g = Sudoku()
        self.s = SudokuSolver()

    def get_sudoku(self):
        result = ''
        sg = SudokuGenerator()
        self.g.generate_board()
        board = self.g.get_partial_sudoku_matrix()
        self.s.solve_sudoku(board)
        if str(self.s) == str(self.g):
            self.g.print_grid()

            solution = input('Would you like the solution? (type "y" for Yes and "n" for No)\n')
            if solution.lower() == 'y':
                print(self.s)
            else:
                print('Ok, goodbye!')
        else:
            sg.get_sudoku()

