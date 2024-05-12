def solution(n):
    answer = 0
    next_num = n
    while True:
        next_num += 1
        if format(n, 'b').count('1') == format(next_num, 'b').count('1'):
            answer += next_num
            break
    return answer