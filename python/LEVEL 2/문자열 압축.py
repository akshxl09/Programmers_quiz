def solution(s):
    if len(s) <=2:
        return len(s)
    answer=[]
    for i in range(1,len(s)//2+1):
        arr=[]
        tmp=0
        for j in range(i,len(s),i):
            arr.append(s[tmp:j])
            tmp=j
        arr.append(s[tmp:])
        
        cnt=1
        strr=''
        for j in range(len(arr)):
            if j < len(arr)-1 and arr[j]==arr[j+1]:
                cnt+=1
            
            else:
                if cnt==1:
                    strr+=arr[j]
                else:
                    strr+=str(cnt) + arr[j]
                    cnt=1
        answer.append(len(strr))
    return min(answer)