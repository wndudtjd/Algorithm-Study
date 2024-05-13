def solution(s):
    answer = []
    cnt = 0
    zero = 0
    while True:
        if s == '1':
            break
        zero += s.count('0')
        s = s.translate({ord('0') : None})
        s = format(len(s), 'b')
        cnt += 1
    answer = [cnt, zero]
    return answer