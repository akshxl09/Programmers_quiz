def solution(prices):
    answer=[0] * len(prices)
    stack=[]
        
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            tmp = stack.pop()
            answer[tmp]=i-tmp 
        stack.append(i)
    
    while stack:
        tmp=stack.pop()
        answer[tmp]=len(prices)-tmp-1
        
        
    return answer
'''
from collections import deque
def solution(prices):
    answer=[]
    que=deque(prices)
    while que:
        time=0
        price = que.popleft()
        
        for i in que:
            time+=1
            if price > i:
                break
        answer.append(time)
        
    return answer
'''