from collections import deque
def solution(skill, skill_trees):  
    answer=0
    for i in skill_trees:
        flag=1
        cnt=0
        queue=deque(i)
        while queue:
            tmp=queue.popleft()
            if tmp in skill:
                if skill.index(tmp)==cnt:
                    cnt+=1
                else:
                    flag=0
                    break
        if flag:
            answer+=1

    return answer