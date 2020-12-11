def addBorder(picture):
    output = list(map(lambda x: "*" + x + "*",picture))
    maxSize = 0
    for i in picture:
        if len(i) > maxSize:
            maxSize = len(i)
    maxSize += 2
    return [maxSize * "*"] + output + [maxSize * "*"]