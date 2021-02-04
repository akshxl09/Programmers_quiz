def solution(arr):
    
    a = []
    
    for i in arr:
        if not a or a[-1] != i:
            a.append(i)
    return a