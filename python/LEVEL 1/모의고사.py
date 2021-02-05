def solution(answers):
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    cnt=[0]*3
    answer=[]
    
    for idx, i in enumerate(answers):
        if i==a[idx%len(a)]:
            cnt[0]+=1
        if i==b[idx%len(b)]:
            cnt[1]+=1
        if i==c[idx%len(c)]:
            cnt[2]+=1
        
    x=max(cnt)
    for idx, i in enumerate(cnt):
        if i==x:
            answer.append(idx+1)
    return answer