## 처음 내가 작성한 코드
def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n - 1
            ans += 1
        else:
            break
    return ans

## 수정한 코드
def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            ans += 1
    return ans

## 다른사람이 풀이한 코드
def solution(n):
    return bin(n).count('1')