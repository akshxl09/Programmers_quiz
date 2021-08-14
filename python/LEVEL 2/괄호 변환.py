def correct(s):
    stack=[]
    if s=='':
        return 0
    for i in s:
        if i == '(' or not stack:
            stack.append(i)
        else:
            if stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
    if stack:
        return 0
    return 1

def balanced(s):
    cnt_1=0
    cnt_2=0
    
    for idx, i in enumerate(s):
        if i=='(':
            cnt_1+=1
        else:
            cnt_2+=1
        if cnt_1==cnt_2:
            return idx

def reverse(s):
    temp=''
    for i in s:
            if i=='(':
                temp+=')'
            else:
                temp+='('
    return temp

def solution(p):
    if p=='':
        return p
    
    idx = balanced(p)+1
    u = p[:idx]
    v = p[idx:]

    if correct(u):
        return u + solution(v)
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'
        temp=reverse(u[1:-1])
        tmp += temp
        
        return tmp
