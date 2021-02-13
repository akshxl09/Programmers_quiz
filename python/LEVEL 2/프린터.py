from collections import deque
def solution(priorities, location):
    queue=deque(priorities)
    
    answer=0
    while queue:
        tmp=queue.popleft()
        location-=1
        if queue and max(queue) > tmp:
            queue.append(tmp)
            if location==-1:
                location=len(queue) -1
        else:
            answer+=1
            if location==-1:
                return answer