from sudoku_generator import SudokuGenerator

s = SudokuGenerator()
play = input('Hello! Welcome to Sudoku! \nDo Want a Sudoku Board? (type "y" for Yes and "n" for No) \n')
if play.lower() == 'y':
    s.get_sudoku()
else:
    print('Ok, goodbye!')

solution = input('Would you like the solution? (type "y" for Yes and "n" for No)\n')
if solution.lower() == 'y':
    s.print_solution()
else:
    print('Ok, goodbye!')

print('\n')
print(s)