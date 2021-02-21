def solution(clothes):
    dic={}
    answer=1
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]]+=1
        else:
            dic[cloth[1]]=1
    
    for i in dic:
        print(dic[i])
        answer*=dic[i]+1
    
    return answer-1