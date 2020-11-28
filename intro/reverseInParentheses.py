def reverseInParentheses(inputString):
    allParenthesis = []
    leftParenthesis = []
    
    for i in range(len(inputString)):
        if(inputString[i] == "("):
            leftParenthesis.append(i)
        elif(inputString[i] == ")"):
            allParenthesis.append((leftParenthesis[-1],i))
            leftParenthesis = leftParenthesis[:-1]
    
    for j in allParenthesis:
        left, right = j
        inputString = inputString[:left] + inputString[left:right][::-1]+ inputString[right:]
    
    return inputString.replace(')', '').replace('(', '')