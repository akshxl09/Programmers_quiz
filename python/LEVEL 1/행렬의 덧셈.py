def solution(arr1, arr2):
    for idx, i in enumerate(arr1):
        for cnt, j in enumerate(i):
            arr2[idx][cnt]+=j
    
    return arr2

'''
def solution(arr1, arr2):
    answer=[]
    
    for a,b in zip(arr1,arr2):
        tmp=[]
        for i,j in zip(a,b):
            tmp.append(i+j)
        answer.append(tmp)
    return answer
'''