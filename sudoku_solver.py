class SudokuSolver:
    """
    Solves a classic sudoku board (9x9) via the backtracking algorithm
    """
    def __init__(self):
        self.board = []
        self.solved_board = []
        self.solution = ''

    def solve_sudoku(self, board):
        """
        Solves a sudoku matrix using backtracking algorithm
        :param board: sudoku board in a 9x9 matrix -- with zeros for the empty spaces
        :return: True or False if the matrix is solved or not
        """
        s = SudokuSolver()
        empty = s.find_empty_cells(board)

        # If there are no more empty spots on the board, it is solved
        if not empty:
            return True

        # Checks the validity of every possible number (1-9) in each position
        for nums in range(9):
            if s.isvalid(board, empty, nums + 1):
                board[empty[0]][empty[1]] = nums + 1
                if s.solve_sudoku(board):  # recursive step
                    for line in board:
                        self.solved_board.append(line)
                    return True
                # If the number is wrong, we set it back to 0 (empty)
                board[empty[0]][empty[1]] = 0
        return False

    @staticmethod
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
    def isvalid(grid, pos, n):
        """
        Checks if a number is valid in that coordinate on the sudoku board
        :param grid: sudoku board
        :param pos: coordinate for that number (tuple)
        :param n: positive integer from 1-9
        :return: True or False if the number is in valid position
        """
        # Compares number coordinates to check if this is the number we are looking for
        for i in range(9):
            if grid[i][pos[1]] == n and (i, pos[1]) != pos:
                return False

        # Compares row and number, this way we can know if the number is in the correct row
        # but in the incorrect spot
        for j in range(9):
            if grid[pos[0]][j] == n and (pos[0], j) != pos:
                return False

        start_i = pos[0] - pos[0] % 3
        start_j = pos[1] - pos[1] % 3

        # Checking if the number and coordinates are valid for each number
        # in the sub-matrix (3x3) squares
        for x in range(3):
            for y in range(3):
                if grid[start_i + x][start_j + y] == n and (start_i+x, start_j+y) != pos:
                    return False
        # If all tests pass the number is valid in that position
        return True

    def __str__(self):
        """
        returns solved matrix in string form for easier comparison
        """
        s = ''
        for line in self.solved_board:
            s += str(line) + '\n'
        self.solution = s[:]
        return s
