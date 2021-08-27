def solution(n, words):
    temp = [words[0]]
    
    for i in range(1, len(words)):
        if words[i-1][-1] == words[i][0] and words[i] not in temp:
            temp.append(words[i])
        else:
            break
    if len(temp)==len(words):
        return [0,0]
    i += 1
    if i%n == 0:
        return [n,i//n]
    else:
        return [i%n,(i//n)+1]
        