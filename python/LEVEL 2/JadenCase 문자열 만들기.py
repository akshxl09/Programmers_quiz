def solution(s):
    a = list(s.split(" "))
    b=[]
    
    for i in a:
        b.append(i.capitalize())
    
    return " ".join(b)