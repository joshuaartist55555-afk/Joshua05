def solveNQueens(n):
    def backtrack(row):
        if row == n:
            board = []
            for r in range(n):
                line = ['.'] * n
                line[queens[r]] = 'Q'
                board.append("".join(line))
            results.append(board)
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            queens[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            backtrack(row + 1)
            
            # backtrack
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    results = []
    queens = [-1] * n  # queens[i] = column index of queen in row i
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    backtrack(0)
    return results
