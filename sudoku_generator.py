from sudoku import Sudoku
from sudoku_solver import SudokuSolver


class SudokuGenerator:
    """
    Generates a classic 9x9 grid sudoku that has a single solution and outputs the solvable grid and its solution
    """
    def __init__(self):
        self.g = Sudoku()
        self.s = SudokuSolver()

    def get_sudoku(self):
        """
        Gets a random sudoku grid (unsolved) and its expected solution. It then solves the sudoku and checks if the
        grid is solvable and that the result from solving is the same as expected (meaning that it has a single
        solution)
        """
        sg = SudokuGenerator()
        self.g.generate_board()
        board = self.g.get_partial_sudoku_matrix()
        self.s.solve_sudoku(board)
        # Comparing string outputs from the original grid and the solved grid, if they match output grid, if not gets
        # a new grid and repeats
        if str(self.s) == str(self.g):
            self.g.print_grid()

            solution = input('Would you like the solution? (type "y" for Yes and "n" for No)\n')
            if solution.lower() == 'y':
                print(self.s)
            else:
                print('Ok, goodbye!')
        else:
            sg.get_sudoku()
