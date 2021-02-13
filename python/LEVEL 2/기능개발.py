def solution(progresses, speeds):
    answer=0
    list_=[]
    while progresses:
        if progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            answer+=1
        else:
            if answer:
                list_.append(answer)
                answer=0
            for i in range(len(progresses)):
                progresses[i]+=speeds[i]
    list_.append(answer)
    return list_