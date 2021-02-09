def solution(numbers, hand):
    answer=''
    left=10
    right=12
    for i in numbers:
        l_cnt=0
        r_cnt=0
        if i==1 or i==4 or i==7:
            answer+='L'
            left=i
        elif i==3 or i==6 or i==9:
            answer+='R'
            right=i
        else: 
            if i==0:
                i=11
            tmp=left
            while tmp!=i:
                if tmp+1==i:
                    tmp+=1
                    l_cnt+=1
                elif i<tmp:
                    tmp-=3
                    l_cnt+=1
                elif i>tmp:
                    tmp+=3
                    l_cnt+=1
            
            tmp=right
            while tmp!=i:
                if tmp-1==i:
                    tmp-=1
                    r_cnt+=1
                elif i<tmp:
                    tmp-=3
                    r_cnt+=1
                elif i>tmp:
                    tmp+=3
                    r_cnt+=1
                
            if r_cnt > l_cnt:
                answer+='L'
                left=i
            elif r_cnt < l_cnt:
                answer+='R'
                right=i
            else:
                if hand=='left':
                    answer+='L'
                    left=i
                else:
                    answer+='R'
                    right=i
    return answer