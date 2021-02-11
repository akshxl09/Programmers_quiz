def solution(dartResult):
    score=[0,0,0]
    i=0
    cnt=-1
    sdt=['S','D','T']
    while i<len(dartResult):
        if dartResult[i] in sdt:
            score[cnt]**=sdt.index(dartResult[i])+1
        elif dartResult[i]=='#':
            score[cnt]*=-1
        elif dartResult[i]=='*':
            score[cnt]*=2
            if cnt!=0:
                score[cnt-1]*=2
        else:
            cnt+=1
            if dartResult[i+1]=='0':
                score[cnt]+=10
                i+=1
            else:
                score[cnt]+=int(dartResult[i])
        i+=1
            
    return sum(score)