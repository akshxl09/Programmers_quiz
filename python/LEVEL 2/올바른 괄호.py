def solution(s):
    stack = []
    
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        
            else:
                stack.append(i)
            
    if stack:
        return False
    else:
        return True