def almostIncreasingSequence(sequence):
    
    count = 0
    for i in range(1,len(sequence)):
        
        if sequence[i] <= sequence[i - 1]:
            count+=1
            
            if i > 1 and sequence[i] <= sequence[i - 2]:
                if i < len(sequence) - 1 and sequence[i + 1] <= sequence[i - 1]:
                    return False
            
    return count <= 1

# def almostIncreasingSequence(sequence):
#     c = 0
#     for i in range(len(sequence)-1):
#         if sequence[i] >= sequence[i+1]: c += 1
#         if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: c += 1
#     return c < 3