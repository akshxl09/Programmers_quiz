def solution(id_list, report, k):
    reported = {}
    answer = {}
    report = list(set(report))
    for id in id_list:
        reported[id] = 0
        answer[id] = 0
    
    for id in report:
        tmp = id.split(' ')
        reported[tmp[1]] += 1
    
    for id in report:
        tmp = id.split(' ')
        if reported[tmp[1]] >= k:
            answer[tmp[0]] += 1
    
    return list(answer.values())