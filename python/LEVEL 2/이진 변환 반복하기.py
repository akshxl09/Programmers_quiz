def solution(s):
    cnt_1=0
    cnt_2=0
    
    while s!='1':
        cnt_1+=1
        cnt_2+=s.count('0')
        s=s.replace('0','')
        s=bin(len(s))[2:]
    
    return [cnt_1,cnt_2]