from itertools import combinations
def primary(num):
    flag = 1
    for i in range(2, int(sum(num)/2) +1):
        if sum(num)%i == 0:
            flag = 0
            break
    return flag
        
def solution(nums):
    tmp = list(combinations(nums,3))

    return sum(list(map(primary, tmp)))