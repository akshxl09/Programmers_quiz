def check(s):
    stack = []
    for i in s:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        else:
            if stack:
                if i==')' and stack[-1]=='(':
                    stack.pop()
                elif i=='}' and stack[-1]=='{':
                    stack.pop()
                elif i==']' and stack[-1]=='[':
                    stack.pop()
            else:
                stack.append(i)
    if stack:
        return 0
    else:
        return 1
    
def solution(s):
    length = len(s)
    result = 0
    for _ in range(length):
        if check(s):
            result += 1
        s = s[1:] + s[0]
    
    return result