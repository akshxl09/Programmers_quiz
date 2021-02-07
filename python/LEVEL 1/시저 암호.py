def solution(s, n):
    str=""
    #97,65
    for i in s:
        if i==' ':
            str+=' '
        elif ord(i)>=ord('a'):
            str+= chr((ord(i)-ord('a')+n)%26 + ord('a'))
        else:
            str+= chr((ord(i)-ord('A')+n)%26 + ord('A'))

    return str