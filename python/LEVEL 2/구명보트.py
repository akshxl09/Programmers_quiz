from collections import deque
def solution(people, limit):
    answer=0
    people=sorted(people,reverse=True)
    que=deque(people)
    
    while que:
        if len(que) >=2 and que[0] + que[-1]<=limit:
            que.pop()
            que.popleft()
        else:
            que.popleft()
        answer+=1
    
    return answer