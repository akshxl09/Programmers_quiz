def solution(dirs):
    move={'U':1, 'D':-1, 'L':-1, 'R':1}
    answer=[]
    character=[0,0]
    
    for i in dirs:
        if i=='U' or i=='D':
            if character[1]!=5 and character[1]!=-5:
                tmp=[character[0],character[1],character[0],character[1]+move[i]]
                if tmp not in answer and tmp[2:].extend(tmp[0:2]) not in answer:
                    answer.append(tmp)
                character[1]+=move[i]
        else:
            if character[0]!=5 and character[0]!=-5:
                tmp=[character[0],character[1],character[0]+move[i],character[1]]
                if tmp not in answer and tmp[2:].extend(tmp[0:2]) not in answer:
                    answer.append(tmp)
                character[0]+=move[i]
    
    return answer

print(solution('LRLRL'))