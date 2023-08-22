'''https://school.programmers.co.kr/learn/courses/30/lessons/17680'''
def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities :
        if city.lower() in cache :
            answer = answer + 1
            cache.remove(city.lower())
            cache.append(city.lower())
        else :
            answer = answer + 5
            if len(cache) >= cacheSize and cacheSize != 0:
                cache.pop(0)
            if cacheSize != 0 :
                cache.append(city.lower())
    return answer