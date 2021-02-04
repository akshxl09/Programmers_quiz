def solution(s):
    a=len(s)
    if a%2==0:
        a=int(a/2)
        tmp=s[a-1]+s[a]
        return tmp
    else:
        a=int(a/2)
        return s[a]