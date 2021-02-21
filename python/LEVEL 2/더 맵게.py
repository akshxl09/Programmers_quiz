import heapq
def solution(scoville, K):
    heap=scoville
    heapq.heapify(heap)
    cnt=0
    while heap:
        tmp1 = heapq.heappop(heap)
        tmp2 = heapq.heappop(heap)
        
        tmp = tmp1 + tmp2*2
        heapq.heappush(heap,tmp)
        cnt+=1
        
        #print(heap)
        if heap[0] >= K:
            break
        if len(heap)==1:
            return -1
    return cnt