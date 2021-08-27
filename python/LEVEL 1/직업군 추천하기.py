def solution(table, languages, preference):
    answer={'SI':0, 'CONTENTS':0, 'HARDWARE':0, 'PORTAL':0, 'GAME':0}
    job=[]
    
    for i in table:
        tmp = list(map(str,i.split(' ')))
        job.append(tmp[::-1])
    
    for lan, prefer in zip(languages, preference):
        for i in job:
            result = 0
            for j in range(0,5):
                if i[j] == lan:
                    result += (j+1) * prefer
            answer[i[-1]]+=result
    result = sorted(answer.items(), key=lambda x: (-x[1],x[0]))
    
    return result[0][0]