def solution(board, moves): 
    basket = []
    boomCount = 0
    N = len(board)

    for m in moves:
        m = m-1
        i = 0   
         
        while N > i and board[i][m] == 0:
            i += 1

        if i == N:
            continue

        x = board[i][m]
        board[i][m] = 0
        

        if basket and basket[-1] == x:
            del basket[-1]
            boomCount += 2
        else:
            basket.append(x)
               
    return boomCount
