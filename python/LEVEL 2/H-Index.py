def solution(citations):
    n = len(citations)
    tmp = 0
    for h in range(1, n):
        cnt = 0
        for number in citations:
            if number >= h:
                cnt+=1
        if cnt >= h and n-cnt <= h:
            tmp = h
    return tmp

'''
def solution(citations):
    n = len(citations)
    citations = sorted(citations)
    
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    return 0
'''