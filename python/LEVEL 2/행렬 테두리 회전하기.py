def make_matrix(rows, columns):
    matrix = [[0] * columns for _ in range(rows)]

    for i in range(1,rows +1):
        for j in range(1,columns +1):
            matrix[i-1][j-1] = ((i-1) * columns + j)

    return matrix

def solution(rows, columns, queries):
    answer = []
    matrix = make_matrix(rows, columns)
    
    for query in queries:
        tmp = []
        row1 = query[0]-1
        col1 = query[1]-1
        row2 = query[2]-1
        col2 = query[3]-1
        for i in range(col1, col2+1):
            tmp.append(matrix[row1][i])

        for i in range(row1+1, row2+1):
            tmp.append(matrix[i][col2])

        for i in range(col2-1, col1-1, -1):
            tmp.append(matrix[row2][i])

        for i in range(row2-1, row1, -1):
            tmp.append(matrix[i][col1])
        
        answer.append(min(tmp))
        cnt = len(tmp) -1
        
        for i in range(col1, col2+1):
            matrix[row1][i] = tmp[cnt%len(tmp)]
            cnt += 1

        for i in range(row1+1, row2+1):
            matrix[i][col2] = tmp[cnt%len(tmp)]
            cnt += 1

        for i in range(col2-1, col1-1, -1):
            matrix[row2][i] = tmp[cnt%len(tmp)]
            cnt += 1
            
        for i in range(row2-1, row1, -1):
            matrix[i][col1] = tmp[cnt%len(tmp)]
            cnt += 1

    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])