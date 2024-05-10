import numpy as np

def solution(n):
    matrix = np.zeros((n, n), dtype=int)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir = 0
    
    row, col = 0, 0
    for i in range(1, n * n + 1):
        matrix[row, col] = i
        
        next_row = row + directions[current_dir][0]
        next_col = col + directions[current_dir][1]
        
        if (not (0 <= next_row < n and 0 <= next_col < n)) or matrix[next_row, next_col] != 0:
            current_dir = (current_dir + 1) % 4
            next_row = row + directions[current_dir][0]
            next_col = col + directions[current_dir][1]
        
        row, col = next_row, next_col
        
    return matrix.tolist()
print(solution(4))