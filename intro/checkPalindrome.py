def checkPalindrome(inputString):
    middle_index = len(inputString) // 2
    
    if len(inputString) == 1:
        return True
    elif len(inputString) % 2 == 0:
        if inputString[0:middle_index][::-1] == inputString[middle_index:]:
            return True
        else:
            return False
    else:
        if inputString[:middle_index][::-1] == inputString[middle_index + 1:]:
            return True
        else:
            return False