def solution(a, b):
    cnt=0
    sum=0
    while cnt<len(a):
        sum+=a[cnt]*b[cnt]
        cnt+=1
    return sum