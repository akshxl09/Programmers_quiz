def solution(arr, divisor):
    a= []
    for i in arr:
        if i%divisor == 0:
            a.append(i)
    if not a:
        a.append(-1)
    return sorted(a)