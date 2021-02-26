def solution(s):
    number=sorted(list(map(int,s.split())))
    return "%s %s"%(number[0],number[-1])