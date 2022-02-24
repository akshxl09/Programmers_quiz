from itertools import permutations

from pkg_resources import ResolutionError
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


print(solution(80,[[80,20],[50,40],[30,10],[60,30],[20,10],[30,20]]))