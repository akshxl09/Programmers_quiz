def solution(phone_book):
    hash_={}
    
    for number in phone_book:
        hash_[number]=1
    
    for number in phone_book:
        tmp=''
        
        for i in number:
            tmp+=i
            if tmp in hash_ and tmp != number:
                return False
    return True