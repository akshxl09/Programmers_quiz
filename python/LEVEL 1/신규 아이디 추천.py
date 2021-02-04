def check(new_id):
    check='abcdefghijklmnopqrstuvwxyz0123456789-_.'
    tmp=''
    for i in new_id:
        if i in check:
            tmp+=i
    return tmp

def continuous_point(new_id):
    cnt=0
    tmp=''
    for i in new_id:
        if i =='.':
            cnt+=1
        else:
            cnt=0
            
        if cnt>1:
            cnt-=1
            continue
        tmp+=i
    return tmp

def start_finish(new_id):
    
    if new_id=='.':
        return ''
    
    if new_id[0] == '.':
        new_id=new_id[1:]
    
    if new_id[-1] == '.':
        new_id=new_id[:-1]
    
    return new_id


            
def solution(new_id):
    new_id = new_id.lower()
    new_id = check(new_id)
    new_id = continuous_point(new_id)
    new_id = start_finish(new_id)
    
    if not new_id:
        new_id='a'
    
    if len(new_id) >15:
        new_id=new_id[:15]
        new_id=start_finish(new_id)
    
    while len(new_id) < 3:
        new_id=new_id+new_id[-1]
    
    return new_id