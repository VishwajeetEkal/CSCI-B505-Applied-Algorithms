def smallestString(givenWord):
    givenWord = list(givenWord)
    encodeLength = len(givenWord)
    
    itrGivenWord = 0
    while itrGivenWord < encodeLength // 2:
        if givenWord[itrGivenWord] != 'a':
            givenWord[itrGivenWord] = 'a'
            return ''.join(givenWord)
        itrGivenWord += 1
    
    
    givenWord[-1] = 'b'
    return ''.join(givenWord)


print(smallestString("abcddcba"))  
print(smallestString("aaabaaa"))   
