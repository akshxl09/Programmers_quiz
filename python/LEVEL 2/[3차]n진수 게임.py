def zin(cnt, n):
    tmp=[]
    while cnt >= n:
        tmp.append(cnt % n)
        cnt = cnt // n
    tmp.append(cnt)
    return tmp
        
def change(a):
    if a==10: return 'A'
    elif a==11: return 'B'
    elif a==12: return 'C'
    elif a==13: return 'D'
    elif a==14: return 'E'
    elif a==15: return 'F'
    else: return a
    
def solution(n, t, m, p):
    cnt = 0
    answer = []
    tmp = []
    temp = []
    num = p
    for _ in range(t):
        p += m
        
    for _ in range(p):
        tmp = zin(cnt, n)
        cnt += 1
        
        while tmp:            
            temp.append(change(tmp.pop()))
    
    while num < p:
        answer.append(str(temp[num-1]))
        num += m  
    return ''.join(answer)