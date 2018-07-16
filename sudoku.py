from sudoku.sudoku import Board, solver

# Sudoku matrix in vector form:
A = [4,0,0, 0,0,8, 0,0,0, 0,8,0, 0,0,0, 3,0,9, 7,0,0, 0,0,0, 0,2,0, 0,0,0, 2,0,7, 1,0,0, 0,6,0, 0,0,5, 0,0,8, 0,9,1, 0,0,0, 0,6,0, 0,0,8, 0,4,2, 0,0,0, 0,0,2, 1,0,0, 0,8,0, 6,0,0, 0,0,0, 0,0,7]

# Initialize a bord with the above vector:
b = Board(A)
print(b)

# Find a solution:
sol = solve(b)
print(sol)
