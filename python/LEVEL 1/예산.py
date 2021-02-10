def solution(d, budget):
    sum=0
    cnt=0
    for i in sorted(d):
        if sum+i <= budget:
            sum+=i
            cnt+=1
        
        if sum==budget:
            break
    return cnt