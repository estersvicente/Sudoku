from sudoku_generator import SudokuGenerator

s = SudokuGenerator()
play = input('Hello! Welcome to Sudoku! \nDo Want a Sudoku Board? (type "y" for Yes and "n" for No) \n')
if play.lower() == 'y':
    s.get_sudoku()
else:
    print('Ok, goodbye!')
