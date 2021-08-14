def solution(name):
    tmp=list(map(str,name))
    cnt=0
    for i in tmp:
        if i!='A':
            cnt+=1
    answer=0
    idx=0

    while True:
        if tmp[idx]!='A':
            answer+=min((ord(tmp[idx])-ord('A')), (ord('Z')-ord(tmp[idx])+1))
            tmp[idx]='A'
            cnt-=1
        if cnt==0:
            return answer
        left=idx
        right=idx
        while left!=len(tmp)-1:
            left+=1
            if tmp[left]!='A':
                break

        while True:
            right-=1
            if tmp[right]!='A':
                break

        if abs(idx-left) > abs(idx-right):
            answer+=abs(idx-right)
            idx=right
        else:
            answer+=abs(idx-left)
            idx=left

print(solution("BBABAAAB"))