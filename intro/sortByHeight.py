def sortByHeight(a):

    output = list(filter(lambda x: x!= -1, sorted(a)))

    for i in range(len(a)):
        if a[i] == -1:
            output.insert(i,a[i])
    
    return output
