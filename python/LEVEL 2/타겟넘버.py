from collections import deque    
def solution(numbers, target):
    que=deque([(0,0)])
    cnt=0
    while que:
        idx, answer=que.popleft()
        
        if idx == len(numbers):
            if answer == target:
                cnt+=1
        else:
            que.append((idx+1,answer+numbers[idx]))
            que.append((idx+1,answer-numbers[idx]))
    return cnt