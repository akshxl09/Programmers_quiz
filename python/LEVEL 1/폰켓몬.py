def solution(nums):
    length=len(nums)//2
    arr=[]
    cnt=0

    for i in nums:
        if cnt==length:
            break
        if i not in arr:
            arr.append(i)
            cnt+=1
    return len(arr)