from itertools import permutations
def solution(numbers):
    arr = list(numbers)
    ans = []
    answer = 0
    for i in range(1, len(arr)+1):
        tmp = list(permutations(arr, i))
        for num in tmp:
            ans.append(int(''.join(num)))

    for num in set(ans):
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if num%i==0:
                    break
            else:
                answer += 1
    return answer