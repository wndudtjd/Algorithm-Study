def solution(n, words):
    
    checked = [words[0]]
    
    for i in range(1,len(words)):
        #i번째 단어와 첫 글자와 i-1번째 단어의 마지막 글자랑 비교 
        if words[i][0] == words[i-1][-1] and words[i] not in checked:
            checked.append(words[i])
        else:
            return [(i%n)+1, (i//n)+1]

    return [0,0]