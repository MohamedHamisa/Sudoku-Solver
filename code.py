class Solution:
    def solveSudoku(self, board):
        def dfs(board, stack1, stack2):
            if not stack1: return
            x, y = stack1.pop()
            stack2.append((x, y))
            box = [board[x//3*3+i][y//3*3+j] for i in range(3) for j in range(3)]
            row = [board[x][j] for j in range(9)]
            col = [board[i][y] for i in range(9)]
            for i in "123456789":
                if not any([i in box, i in col, i in row]):
                    board[x][y] = i
                    dfs(board, stack1, stack2)
                    if not stack1: return
            board[x][y] = "."
            pos = stack2.pop()
            stack1.append(pos)
        
        stack1 = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]
        stack2 = []
        dfs(board, stack1, stack2)


 
