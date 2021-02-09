def solution(n):
    if n**(1/2) - int(n**(1/2))==0: #n**(1/2)%1==0 일 경우도 정수.
        return (n**(1/2)+1)**2
    
    return -1