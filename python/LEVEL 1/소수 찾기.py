def solution(n):
    arr = [True] * (n+1)
    
    for i in range(2, n+1):
        if arr[i] == True:
            j = 2
            
            while i*j <= n:
                arr[i*j] = False
                j += 1
    
    answer = 0
    
    for i in range(len(arr)):
        if arr[i] == True:
            answer += 1
            
    return answer - 2