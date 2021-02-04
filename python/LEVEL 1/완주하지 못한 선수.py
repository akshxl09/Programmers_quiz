def solution(participant, completion):
    dict={}
    
    for check in participant:
        if check not in dict:
            dict[check]=1
        else:
            dict[check]+=1
        
    for check in completion:
        if check in dict:
            dict[check]-=1
            if dict[check]==0:
                del dict[check]
    return list(dict.keys())[0]