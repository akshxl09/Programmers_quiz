def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        cnt=0
        answer_tmp=[]
        while cnt<len(arr2[0]):
            tmp=0
            for j in range(len(arr2)):
                tmp += arr1[i][j] * arr2[j][cnt]
            cnt+=1
            answer_tmp.append(tmp)
        answer.append(answer_tmp)
    
    return answer