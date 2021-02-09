def solution(n):
    answer=''
    list_=sorted(list(str(n)), reverse=True)
    for i in list_:
        answer+=i
    return int(answer)