def solution(brown, yellow):
    cnt=1
    while yellow//cnt >= cnt:
        if yellow%cnt==0:
            if brown == ((yellow//cnt)*2) + (cnt+2)*2:
                return [yellow//cnt+2,cnt+2]
        cnt+=1