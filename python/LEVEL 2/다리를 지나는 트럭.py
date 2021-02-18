from collections import deque
def solution(bridge_length, weight, truck_weights):
    que = deque([[truck_weights[0],1]])
    cnt=1
    sum=truck_weights[0]

    i=1
    while que:
        cnt+=1
        
        if cnt - que[0][1] == bridge_length:
            tmp=que.popleft()
            sum-=tmp[0]

        
        if i < len(truck_weights) and sum + truck_weights[i] <= weight:
            que.append([truck_weights[i],cnt])
            sum+=truck_weights[i]
            i+=1
        
    return cnt