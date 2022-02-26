"""
from itertools import permutations
def solution(k, dungeons):

    result = 0
    for dungeon in permutations(dungeons, len(dungeons)):
        tired = k
        cnt = 0
        for lst in dungeon:
            if tired >= lst[0]:
                tired -= lst[1]
                cnt += 1
        if cnt > result:
            result = cnt
    
    return result
"""
answer = 0
def dfs(k, dungeons, visited, cnt):
    global answer
    if k <= 0: return
    if cnt > answer: 
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = 1
            dfs(k-dungeons[i][1], dungeons, visited, cnt+1)
            visited[i] = 0

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    dfs(k, dungeons, visited, 0)

    return answer 



print(solution(80,[[80,20],[50,40],[30,10],[60,30],[20,10],[30,20]]))