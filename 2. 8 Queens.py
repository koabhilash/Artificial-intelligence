def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = '.'
    
    return False

def solve(n=8):
    board = [['.' for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0, n):
        print_board(board)
    else:
        print("No solution exists")

solve()
