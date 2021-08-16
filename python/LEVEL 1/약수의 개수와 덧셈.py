def solution(left, right):
    total=0
    for i in range(left,right+1):
        cnt=0
        for num in range(1,i+1):
            if i%num==0:
                cnt+=1
        if cnt%2==0:
            total+=i
        else:
            total-=i
    return total