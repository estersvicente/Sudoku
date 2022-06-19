class SudokuSolver:
    """
    Solves a classic sudoku board (9x9) via the backtracking algorithm
    """
    def __init__(self, board):
        self.board = board

    def solve_sudoku(self):
        """
        Solves a classic sudoku board using backtracking algorithm
        :return: solved board
        """

        # Find all empty spaces (0) in board
        # if there are no more empty spaces (0) the board is solved
        empty_space = find_empty_cells(self.board)
        if not empty_space:
            return True

        for number in range(9):
            if isvalid(self.board, empty_space, number + 1):
                self.board[empty_space[0]][empty_space[1]] = number + 1

                if SudokuSolver.solve_sudoku(self):
                    return True

                # If number is in the wrong stop set it back to empty (0)
                self.board[empty_space[0]][empty_space[1]] = 0
        return False

    def print_solution(self):
        """
        Prints solved sudoku grid in a string form
        """
        boardString = ''
        for i in range(9):
            for j in range(9):
                boardString += str(self.board[i][j]) + ' '
                if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                    boardString += '| '

                if j == 8:
                    boardString += '\n'

                if j == 8 and (i + 1) % 3 == 0 and i + 1 != 9:
                    boardString += '- - - - - - - - - - - \n'
        print(boardString)

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
                position = (i, j)
                return position


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
