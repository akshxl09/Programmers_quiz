def solution(n, m):
    if n > m:
        n ,m = m, n
    a=n
    b=m

    while m%n>0:
        n, m=m%n, n
    
    return [n,a*b/n]