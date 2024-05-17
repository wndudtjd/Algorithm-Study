def solution(operations):
    answer = []
    
    for operation in operations:
        command, number = operation.split(" ")
        number = int(number)
        
        if command == 'I':
            answer.append(number)
        elif command == 'D':
            if answer:
                if number == 1:
                    answer.remove(max(answer))
                elif number == -1:
                    answer.remove(min(answer))
    
    if not answer:
        return [0, 0]
    
    return [max(answer), min(answer)]