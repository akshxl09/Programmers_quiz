def solution(lottos, win_nums):
    cnt=0
    list_=[6,5,4,3,2,1,0]
    for i in win_nums:
        if i in lottos:
            cnt+=1
    tmp=lottos.count(0)
    
    answer_1 = list_.index(cnt+tmp) + 1
    if answer_1 > 6:
        answer_1 = 6
    answer_2 = list_.index(cnt) + 1
    if answer_2 > 6:
        answer_2 = 6
    return [answer_1,answer_2]