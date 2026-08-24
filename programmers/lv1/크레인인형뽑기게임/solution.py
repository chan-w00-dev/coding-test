def solution(board, moves): 
    basket = []
    boomCount = 0
    N = len(board)

    for m in moves:
        j = m-1
        i = next((i for i, row in enumerate(board) if row[j] != 0), N)

        if i == N:
            continue

        x = board[i][j]
        board[i][j] = 0
        

        if basket and basket[-1] == x:
            del basket[-1]
            boomCount += 2
        else:
            basket.append(x)
               
    return boomCount
