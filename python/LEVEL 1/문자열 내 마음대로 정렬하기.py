def solution(strings, n):
    arr=[]
    answer=[]
    for i in strings:
        arr.append(i[n])

    strings=sorted(strings)
    arr=sorted(arr)
    
    for i in arr:
        for j in strings:
            if j[n]==i:
                answer.append(j)
                strings.remove(j)
                break
    
    return answer