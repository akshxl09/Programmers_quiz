from itertools import combinations
from collections import Counter
def solution(orders, course):
    result = []
    
    for num in course:
        tmp = []
        for order in orders:
            tmp.extend(list(combinations(sorted(order), num)))
        
        answer = Counter(tmp)
        if answer:
            for key, value in answer.items():
                if value > 1 and value == max(list(answer.values())):
                    result.append(''.join(key))
    return sorted(result)