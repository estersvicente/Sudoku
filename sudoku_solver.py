class SudokuSolver:
    """
    Solves a classic sudoku board (9x9) via the backtracking algorithm
    """
    def __init__(self):
        self.board = []
        self.solved_board = []

    def solve_sudoku(self, board):
        """
        Solving a classic Sudoku by using backtracking algorithm
        :param board: 9x9 sudoku board
        :return: solved sudoku board
        """
        s = SudokuSolver()
        empty = s.find_empty_cells(board)
        if not empty:  # no empty spots are left so the board is solved
            return True

        for nums in range(9):
            if s.isvalid(board, empty, nums + 1):
                board[empty[0]][empty[1]] = nums + 1

                if s.solve_sudoku(board):  # recursive step
                    for line in board:
                        self.solved_board.append(line)
                    return True
                board[empty[0]][empty[1]] = 0  # this number is wrong so we set it back to 0
        return False

    @staticmethod
    # Functions used to solve the board and check valid values
    def find_empty_cells(grid):
        """
        Finds empty cell on a sudoku grid (represented by 0)
        :param grid: 9x9 sudoku grid with 0 representing an empty cell
        :return: the position of the empty cell as a tuple pair
        """
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)

    @staticmethod
    def isvalid(grid, position, number):
        """
        Checks if a number is valid in that coordinate on the sudoku board
        :param grid: sudoku board
        :param position: coordinate for that number (tuple)
        :param number: positive integer from 1-9
        :return: True or False if the number is in valid position
        """
        # Compares number coordinates to check if this is the number we are looking for
        for i in range(9):
            if grid[i][position[1]] == number and (i, position[1]) != position:
                return False

        # Compares row and number, this way we can know if the number is in the correct row
        # but in the incorrect spot
        for j in range(9):
            if grid[position[0][j]] == number and (position[0], j) != position:
                return False

        start_i = position[0] - position[0] % 3
        start_j = position[1] - position[1] % 3

        # Checking if the number and coordinates are valid for each number
        # in the sub-matrix (3x3) squares
        for x in range(3):
            for y in range(3):
                if grid[start_i + x][start_j + y] == number and (start_i+x, start_j+y) != position:
                    return False
        # If all tests pass the number is valid in that position
        return True

    def __str__(self):
        s = ''
        for line in self.solved_board:
            s += str(line) + '\n'
        return s
