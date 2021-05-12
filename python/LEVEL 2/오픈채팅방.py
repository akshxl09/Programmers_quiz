def solution(record):
    dic={}
    answer=[]
    for content in record:
        tmp = list(content.split(' '))
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            dic[tmp[1]] = tmp[2]
    
    for content in record:
        tmp = list(content.split(' '))
        if tmp[0] == 'Enter':
            answer.append("%s님이 들어왔습니다." %dic[tmp[1]])
        elif tmp[0] == 'Leave':
            answer.append("%s님이 나갔습니다." %dic[tmp[1]])
    return answer