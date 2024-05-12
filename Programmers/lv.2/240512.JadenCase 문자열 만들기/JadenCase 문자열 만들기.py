def solution(s):
    answer = ''
    s_list = s.split(" ")
    for i in range(len(s_list)):
        # capitalize : 첫글자를 대문자로 만들어주고 나머지는 소문자로 만들어주는 파이썬 내장 함수
        s_list[i]=s_list[i].capitalize()
        answer=' '.join(s_list)
    print(answer)
    return answer