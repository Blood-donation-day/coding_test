def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]
    for win, lose in results:
        matrix[win-1][lose-1] = True
        matrix[lose-1][win-1] = False
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[j][i] == None:
                    continue
                    
                if matrix[j][i] == matrix[i][k]:
                    matrix[j][k] = matrix[j][i]
                    matrix[k][j] = not matrix[j][i]
                    
    answer = 0
    for i in range(n):
        if None in matrix[i][:i] + matrix[i][i+1:]:
            continue
        answer += 1
    return answer

