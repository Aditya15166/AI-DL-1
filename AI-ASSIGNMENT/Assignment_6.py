# Code for the 8-Queens Problem using Backtracking

def is_safe(board, row, col, n):
    """
    Function to check if it's safe to place a queen at board[row][col]
    """

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    """
    Function to solve the N-Queens problem using backtracking.
    It places queens one by one in different columns and checks if it is safe to place them.
    """

    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Try placing a queen in all rows one by one in this column
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recursively place the rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # If placing queen at board[i][col] doesn't lead to a solution, remove the queen (backtrack)
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column, return False
    return False

def print_solution(board, n):
    """
    Function to print the solution.
    """
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))

def solve_8_queens():
    n = 8  # Size of the chessboard (8x8 for the 8-queens problem)
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print_solution(board, n)
    else:
        print("No solution exists")

# Solve the 8-Queens problem
solve_8_queens()
