def solution(x, n):
    answer=[]
    tmp=x
    for _ in range(n):
        answer.append(x)
        x+=tmp
    return answer