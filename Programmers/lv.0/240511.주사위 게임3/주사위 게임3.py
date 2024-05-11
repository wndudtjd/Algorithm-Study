# 내가짠 코드
def solution(a, b, c, d):
    answer = 0
    origin = [a, b, c, d]
    arr = list(set(origin))
    
    frequency = {}
    for num in origin:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    if len(arr) == 4:
        answer = min(arr)
    elif len(arr) == 3:
        for num, count in frequency.items():
            if count == 2:
                p = num
            elif count == 1:
                if 'q' not in locals():
                    q = num
                else:
                    r = num
        answer = q * r
    elif len(arr) == 2:
        if max([origin.count(num) for num in arr]) > 2:
            p = max(origin, key=origin.count)
            q = min(origin, key=origin.count)
            answer = pow(((10 * p) + q), 2)
        else:
            answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))  
    elif len(arr) == 1:
        answer = 1111 * arr[0]
    print(answer)
    return answer

# 다른사람이 짠 코드
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)