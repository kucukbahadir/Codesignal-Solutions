def makeArrayConsecutive2(statues):
    count = 0
    
    for i in range(min(statues),max(statues) + 1):
        if i not in statues:
            count += 1
    return count