def solution(str1, str2):
    t1=[str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    t2=[str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    s1={}
    s2={}
    for i in t1:
        if i not in s1:
            s1[i]=1
        else:
            s1[i]+=1
    
    for i in t2:
        if i not in s2:
            s2[i]=1
        else:
            s2[i]+=1
    cnt1=0
    cnt2=0
    for i in s1:
        if i in s2:
            cnt1+=min(s1[i],s2[i])
    
    for i in s1:
        if i in s2:
            cnt2+=max(s1[i],s2[i])
        else:
            cnt2+=s1[i]
    for i in s2:
        if i not in s1:
            cnt2+=s2[i]
    print(cnt1,cnt2)
    return int(cnt1/cnt2*65536) if cnt2!=0 else 65536