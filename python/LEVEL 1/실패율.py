def solution(N, stages): 
    dict={}
    answer={}
    for i in range(1,N+2):
        dict[i]=0

    for i in stages:
            dict[i]+=1
        
    total=sum(dict.values())
    for i in range(1,N+1):
        if total==0:
            answer[i]=0
            continue
        fail=dict[i]/total
        total-=dict[i]
        answer[i]=fail

    return sorted(answer, key=lambda x: answer[x], reverse=True)
                

