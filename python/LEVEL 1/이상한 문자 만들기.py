def solution(s):
    answer=''
    tmp=0
    
    for i in s:
        if i==' ':
            answer+=i
            tmp=1
            
        elif tmp%2==0:
            answer+=i.upper()
            
        else:
            answer+=i.lower()
        tmp+=1
    
    return answer