'''
The N Queens problem asks you to place N chess queens on an N×N chessboard so that no two queens can attack each other. In chess, a queen can move any number of squares along a row, column, or diagonal. Therefore, the challenge is to put the queens on the board such that:

No two queens share the same row.

No two queens share the same column.

No two queens share the same diagonal.

Your task is to write an algorithm that finds all possible ways to place the N queens on the board following these rules. The solution should return all distinct configurations of the N queens’ positions that satisfy the attacking constraints.

Explanation:

This problem is a classic example of backtracking algorithms, a technique where you build the solution incrementally and backtrack as soon as you detect a conflict. The algorithm proceeds by placing a queen in the first row, then recursively trying to place queens in subsequent rows. At each step, it checks if placing a queen in a given column is safe (not under attack from previously placed queens). If it is safe, the algorithm continues to the next row; if not, it tries another column. When it reaches the last row successfully, a valid solution is found.



'''
def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        # Check same column or diagonals
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)

def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# Example usage:
solutions = solve_n_queens(8)
print(f"Number of solutions: {len(solutions)}")
for sol in solutions:
    print(sol)
