def solution(s):
    check='0123456789'
    flag=True
    for i in s:
        if i not in check:
            flag=False
    
    # return s.isdigit() and (len(s)==4 or len(s)==6) 로 한줄에 가능!
    
    return (len(s)==4 or len(s)==6) and flag