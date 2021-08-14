def solution(s):
    a = s[2:-2].split('},{')
    answer=[]
    tmp=[]
    for i in a:
        tmp.append(i.split(','))
    
    tmp.sort(key = len)

    for i in tmp:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer