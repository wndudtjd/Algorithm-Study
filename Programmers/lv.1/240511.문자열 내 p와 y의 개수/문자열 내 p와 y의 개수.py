def solution(s):
    answer = True
    
    result = s.lower()
    print(result)
    if result.count("p") == result.count("y"):
        answer = True
    else:
        answer = False

    return answer