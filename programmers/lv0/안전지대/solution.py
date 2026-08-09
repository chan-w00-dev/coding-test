def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):

            if board[i][j] == 1:

                for r in range(i-1,i+2):
                    for c in range(j-1,j+2):
                        if 0 <= r < n and 0 <= c < n:
                            if board[r][c] == 0:
                                board[r][c] = 2

    return sum(1 for row in board for i in row if i == 0)
