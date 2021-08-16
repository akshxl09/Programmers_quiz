def grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 50: return 'D'
    else: return 'F'
def solution(scores):
    num = len(scores)
    answer=[]
    for idx in range(num):
        total = 0
        temp = []
        
        for i in range(num):
            temp.append(scores[i][idx])
        
        if max(temp) == scores[idx][idx] and temp.count(max(temp)) == 1:
            answer.append((sum(temp)-scores[idx][idx])/(num-1))
        elif min(temp) == scores[idx][idx] and temp.count(min(temp)) == 1:
            answer.append((sum(temp)-scores[idx][idx])/(num-1))
        else:
            answer.append(sum(temp)/num)
    return ''.join(list(map(grade,answer)))