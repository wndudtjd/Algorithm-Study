def solution(A,B):
    answer = 0
    result_A = sorted(A)
    result_B = sorted(B, reverse=True)
    for i in range(0,len(A)):
        answer += result_A[i] * result_B[i]
    return answer