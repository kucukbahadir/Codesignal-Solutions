def commonCharacterCount(s1, s2):
    output = 0
    
    for i in set(s1):      
        s1_element = s1.count(i)
        s2_element = s2.count(i)
        if s1_element <= s2_element:
            output += s1_element
        else:
            output += s2_element
            
    return output 