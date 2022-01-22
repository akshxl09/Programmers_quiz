def solution(board):
    num_1 = len(board)
    num_2 = len(board[0])
    
    for i in range(1,num_1):
        for j in range(1,num_2):
            if board[i][j] and board[i-1][j] and board[i][j-1] and board[i-1][j-1]:
                if board[i-1][j] == board[i][j-1]:
                    board[i][j] += board[i-1][j-1]
                else:
                    board[i][j] += min(board[i-1][j], board[i][j-1])
    
    return max(map(max, board))**2