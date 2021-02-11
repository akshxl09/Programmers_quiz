def solution(n, arr1, arr2):
    ar1=[]
    ar2=[]
    answer=[]
    for i in arr1:
        ar1.append(format(i,'b'))
    for i in arr2:
        ar2.append(format(i,'b'))
        
    for a,b in zip(ar1,ar2):
        tmp=''
        if max(len(a),len(b)) < n:
            tmp+='0'*(n-max(len(a),len(b)))
        if len(a)>len(b):
            tmp+=a[:len(a)-len(b)]
            a=a[len(a)-len(b):]
        elif len(a)<len(b):
            tmp+=b[:len(b)-len(a)]
            b=b[len(b)-len(a):]
                        
        for i in range(n-len(tmp)):
            if a[i]=='1' or b[i]=='1':
                tmp+='1'
            else:
                tmp+='0'
        answer.append(tmp.replace('1','#').replace('0',' '))
    return answer