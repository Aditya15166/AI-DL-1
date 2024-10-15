# Minimax Algorithm for Tic-Tac-Toe

# Basic Tic-Tac-Toe Minimax Algorithm for Game Playing

def evaluate(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]

    for wc in win_conditions:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != " ":
            return 10 if board[wc[0]] == "X" else -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score
    if " " not in board:
        return 0

    if is_max:
        best = -1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, depth + 1, False))
                board[i] = " "
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, depth + 1, True))
                board[i] = " "
        return best

def find_best_move(board):
    best_val = -1000
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            move_val = minimax(board, 0, False)
            board[i] = " "
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

board = ["X", "O", "X", "O", "O", "X", " ", " ", " "]
best_move = find_best_move(board)
print("Best Move for 'X':", best_move)
