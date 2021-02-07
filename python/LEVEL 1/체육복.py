def solution(n, lost, reserve):
    
    _reserve=list(set(reserve)-set(lost))
    _lost=list(set(lost)-set(reserve))

    check=[0]*len(_lost)
    answer=n-len(_lost)
    for i in _reserve:
        for idx, j in enumerate(_lost):
            if check[idx]>0:
                continue
            if i+1==j or i-1==j:
                check[idx]+=1
                answer+=1
                break
    
    return answer