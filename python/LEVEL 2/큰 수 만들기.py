def solution(number, k):
    answer=[]
    for i in number:
        
        while answer:
            if answer[-1] < i and k>0:
                answer.pop()
                k-=1             
            else:
                break
        answer.append(i)
        
        
    if k>0:
        return "".join(answer[:-k])
        
    return "".join(answer)