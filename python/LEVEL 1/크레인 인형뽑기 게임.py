def solution(board, moves):
    basket=[]
    cnt = 0
    a=len(board)
    for check in moves:   
        for i in range(a):
            if board[i][check-1] != 0:
                basket.append(board[i][check-1])
                board[i][check-1]=0
                break
        if len(basket) > 1 and basket[-1] == basket[-2]:
            del basket[-2:]
            cnt += 2
    
    return cnt