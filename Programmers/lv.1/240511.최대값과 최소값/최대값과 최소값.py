def solution(s):
    answer = ""
    result = s.split(" ")
    arr = []
    for i in result:
        arr.append(int(i))
    answer = str(min(arr)) + " " + str(max(arr))
    return answer