from sudoku import Sudoku

s = Sudoku()
play = input('Hello! Welcome to Sudoku! \nDo Want a Sudoku Board? (type "y" for Yes and "n" for No) \n')
if play.lower() == 'y':
    s.generate_board()
    s.print_grid()
else:
    print('Ok, goodbye!')

solution = input('Would you like the solution? (type Y for Yes and N for No)\n')
if solution.upper() == 'Y':
    print(s)
    