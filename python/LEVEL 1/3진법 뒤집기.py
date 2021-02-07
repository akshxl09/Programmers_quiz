def solution(n):
    a=''
    cnt=1
    sum=0
    
    while n>0:
        a+=str(n%3)
        n=n//3
    
    for i in reversed(a):
        sum+=int(i)*cnt
        cnt*=3
    
    return sum