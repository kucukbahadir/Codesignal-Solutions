def adjacentElementsProduct(inputArray):
    max_element = inputArray[0] * inputArray[1]
    
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i + 1] > max_element:
            max_element = inputArray[i] * inputArray[i + 1]
    return max_element