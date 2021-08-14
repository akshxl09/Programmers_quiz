def solution(cacheSize, cities):
    if cacheSize==0:
        return 5*len(cities)
    cache=[]
    cities=list(map(lambda x: x.lower(),cities))
    answer=0
    
    for city in cities:
        if city in cache:
            answer+=1
            cache.remove(city)
            cache.append(city)
        else:
            answer+=5
            if len(cache)==cacheSize:
                cache.pop(0)    
            cache.append(city)
    return answer