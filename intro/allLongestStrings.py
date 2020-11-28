def allLongestStrings(inputArray):
    
    longest = len(max(inputArray, key=len))
    
    return list(filter(lambda x: len(x) == longest, inputArray))