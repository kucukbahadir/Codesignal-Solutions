def isLucky(n):
    first_half = str(n)[:len(str(n))//2]
    second_half = str(n)[len(str(n))//2:]
    
    return sum(map(int,list(first_half))) == sum(map(int,list(second_half)))