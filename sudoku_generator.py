from sudoku import Sudoku
from sudoku_solver import SudokuSolver
import numpy as np


class SudokuGenerator:
    def __init__(self):
        self.g = Sudoku()
        self.s = SudokuSolver()

    def get_sudoku(self):
        sg = SudokuGenerator()
        mat1 = np.array(self.g.generate_board())
        board = self.g.get_partial_sudoku_matrix()
        mat2 = np.array(self.s.solve_sudoku(board))
        if np.array_equal(mat1, mat2):
            self.g.print_grid()
        else:
            sg.get_sudoku()


    def get_solution(self):
        solution = input('Would you like the solution? (type "y" for Yes and "n" for No)\n')
        if solution.lower() == 'y':
            print(self.s)
        else:
            print('Ok, goodbye!')
