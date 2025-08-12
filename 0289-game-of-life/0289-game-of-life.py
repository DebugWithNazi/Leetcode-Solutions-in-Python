class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        boardUpdate = [[0] * len(board[0]) for _ in range(len(board))]
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                count = 0

                if i < rows-1 and board[i+1][j] == 1:
                    count += 1
                if j< cols-1 and board[i][j+1] == 1:
                    count += 1
                if i> 0 and board[i-1][j] == 1:
                    count += 1
                if j > 0 and board[i][j-1] == 1:
                    count += 1
                if i> 0 and j > 0 and board[i-1][j-1] == 1:
                    count +=1 
                if i< rows-1 and j< cols-1 and board[i+1][j+1] == 1:
                    count +=1
                if i>0 and j<cols-1 and board[i-1][j+1] == 1:
                    count +=1 
                if i<rows-1 and j>0 and board[i+1][j-1] == 1:
                    count +=1      

                if board[i][j] == 0:                   
                    if count == 3:
                        boardUpdate[i][j] = 1
                elif board[i][j] == 1:
                    if count < 2:
                        boardUpdate[i][j] = 0
                    elif count == 2 or count == 3:
                        boardUpdate[i][j] = 1
                    elif count > 3:
                        boardUpdate[i][j] = 0

        for i in range(len(boardUpdate)):
            for j in range(len(boardUpdate[0])):
                board[i][j] = boardUpdate[i][j]

        return board