def matrixElementsSum(matrix):
    zeros = []
    cost_sum  = 0
    
    for line in matrix:
        for x in range(len(line)):
            if line[x] == 0:
                zeros.append(x)
            if x not in zeros:
                cost_sum += line[x]
    
    return cost_sum
            